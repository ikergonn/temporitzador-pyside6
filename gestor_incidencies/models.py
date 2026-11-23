from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class Priority(str, Enum):
    LOW = "baixa"
    MEDIUM = "mitjana"
    HIGH = "alta"
    CRITICAL = "critica"


class Status(str, Enum):
    OPEN = "oberta"
    IN_PROGRESS = "en_proces"
    BLOCKED = "bloquejada"
    CLOSED = "tancada"


@dataclass(slots=True)
class Incident:
    id: str
    title: str
    description: str = ""
    category: str = "general"
    priority: Priority = Priority.MEDIUM
    status: Status = Status.OPEN
    assignee: str = ""
    created_at: str = field(default_factory=utc_now_iso)
    updated_at: str = field(default_factory=utc_now_iso)
    due_date: str = ""
    tags: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Incident":
        return cls(
            id=str(data["id"]),
            title=str(data["title"]),
            description=str(data.get("description", "")),
            category=str(data.get("category", "general")),
            priority=Priority(data.get("priority", Priority.MEDIUM.value)),
            status=Status(data.get("status", Status.OPEN.value)),
            assignee=str(data.get("assignee", "")),
            created_at=str(data.get("created_at", utc_now_iso())),
            updated_at=str(data.get("updated_at", utc_now_iso())),
            due_date=str(data.get("due_date", "")),
            tags=list(data.get("tags", [])),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "priority": self.priority.value,
            "status": self.status.value,
            "assignee": self.assignee,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "due_date": self.due_date,
            "tags": self.tags,
        }

    def touch(self) -> None:
        self.updated_at = utc_now_iso()


@dataclass(slots=True)
class IncidentFilters:
    text: str = ""
    status: Status | None = None
    priority: Priority | None = None

