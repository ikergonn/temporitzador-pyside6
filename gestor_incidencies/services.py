from __future__ import annotations

from dataclasses import replace

from .models import Incident, IncidentFilters, Priority, Status
from .repository import JsonIncidentRepository


class IncidentValidationError(ValueError):
    pass


class IncidentService:
    def __init__(self, repository: JsonIncidentRepository) -> None:
        self.repository = repository

    def list_incidents(self, filters: IncidentFilters | None = None) -> list[Incident]:
        incidents = self.repository.list_all()
        if filters is None:
            return incidents

        text = filters.text.strip().lower()
        if text:
            incidents = [
                incident
                for incident in incidents
                if text in incident.title.lower()
                or text in incident.description.lower()
                or text in incident.category.lower()
                or text in " ".join(incident.tags).lower()
            ]
        if filters.status:
            incidents = [incident for incident in incidents if incident.status == filters.status]
        if filters.priority:
            incidents = [
                incident for incident in incidents if incident.priority == filters.priority
            ]
        return incidents

    def create_incident(
        self,
        title: str,
        description: str = "",
        category: str = "general",
        priority: Priority | str = Priority.MEDIUM,
        assignee: str = "",
        due_date: str = "",
        tags: list[str] | None = None,
    ) -> Incident:
        clean_title = self._require_text(title, "titol")
        incident = Incident(
            id=self.repository.next_id(),
            title=clean_title,
            description=description.strip(),
            category=category.strip() or "general",
            priority=Priority(priority),
            status=Status.OPEN,
            assignee=assignee.strip(),
            due_date=due_date.strip(),
            tags=self._clean_tags(tags or []),
        )
        return self.repository.add(incident)

    def update_incident(self, incident_id: str, **changes: object) -> Incident:
        incident = self.repository.get(incident_id)
        payload = incident.to_dict()
        payload.update(changes)
        payload["title"] = self._require_text(str(payload["title"]), "titol")
        payload["tags"] = self._clean_tags(list(payload.get("tags", [])))
        updated = Incident.from_dict(payload)
        return self.repository.update(updated)

    def change_status(self, incident_id: str, status: Status) -> Incident:
        incident = self.repository.get(incident_id)
        updated = replace(incident, status=status)
        return self.repository.update(updated)

    def close_incident(self, incident_id: str) -> Incident:
        return self.change_status(incident_id, Status.CLOSED)

    def delete_incident(self, incident_id: str) -> None:
        self.repository.delete(incident_id)

    def stats_by_status(self) -> dict[Status, int]:
        stats = {status: 0 for status in Status}
        for incident in self.repository.list_all():
            stats[incident.status] += 1
        return stats

    def _require_text(self, value: str, field_name: str) -> str:
        clean = value.strip()
        if not clean:
            raise IncidentValidationError(f"El camp {field_name} es obligatori")
        return clean

    def _clean_tags(self, tags: list[str]) -> list[str]:
        cleaned = []
        for tag in tags:
            value = str(tag).strip().lower()
            if value and value not in cleaned:
                cleaned.append(value)
        return cleaned

