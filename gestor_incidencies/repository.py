from __future__ import annotations

import json
import re
from pathlib import Path

from .models import Incident


class IncidentNotFoundError(KeyError):
    pass


class JsonIncidentRepository:
    def __init__(self, path: Path, seed_path: Path | None = None) -> None:
        self.path = Path(path)
        self.seed_path = Path(seed_path) if seed_path else None
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self._initialise_file()

    def _initialise_file(self) -> None:
        if self.seed_path and self.seed_path.exists():
            raw = self.seed_path.read_text(encoding="utf-8")
            self.path.write_text(raw, encoding="utf-8")
        else:
            self._write_raw([])

    def list_all(self) -> list[Incident]:
        return sorted(self._read_raw(), key=lambda incident: incident.id)

    def get(self, incident_id: str) -> Incident:
        for incident in self.list_all():
            if incident.id == incident_id:
                return incident
        raise IncidentNotFoundError(incident_id)

    def add(self, incident: Incident) -> Incident:
        incidents = self.list_all()
        if any(existing.id == incident.id for existing in incidents):
            raise ValueError(f"Incident id duplicat: {incident.id}")
        incidents.append(incident)
        self._write_raw(incidents)
        return incident

    def update(self, incident: Incident) -> Incident:
        incidents = self.list_all()
        for index, existing in enumerate(incidents):
            if existing.id == incident.id:
                incident.touch()
                incidents[index] = incident
                self._write_raw(incidents)
                return incident
        raise IncidentNotFoundError(incident.id)

    def delete(self, incident_id: str) -> None:
        incidents = self.list_all()
        remaining = [incident for incident in incidents if incident.id != incident_id]
        if len(remaining) == len(incidents):
            raise IncidentNotFoundError(incident_id)
        self._write_raw(remaining)

    def next_id(self) -> str:
        max_number = 0
        for incident in self.list_all():
            match = re.fullmatch(r"INC-(\d+)", incident.id)
            if match:
                max_number = max(max_number, int(match.group(1)))
        return f"INC-{max_number + 1:04d}"

    def _read_raw(self) -> list[Incident]:
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Fitxer JSON invalid: {self.path}") from exc
        if not isinstance(data, list):
            raise ValueError("El repositori d'incidencies ha de contenir una llista JSON")
        return [Incident.from_dict(item) for item in data]

    def _write_raw(self, incidents: list[Incident]) -> None:
        payload = [incident.to_dict() for incident in incidents]
        tmp_path = self.path.with_suffix(self.path.suffix + ".tmp")
        tmp_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        tmp_path.replace(self.path)

