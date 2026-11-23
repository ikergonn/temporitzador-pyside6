from __future__ import annotations

from PySide6.QtWidgets import QDialog

from ..models import Incident, Priority, Status
from .ui_incident_dialog import Ui_IncidentDialog


class IncidentDialog(QDialog, Ui_IncidentDialog):
    def __init__(self, parent=None, incident: Incident | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._incident = incident

        for priority in Priority:
            self.priority_combo.addItem(priority.value, priority)
        for status in Status:
            self.status_combo.addItem(status.value, status)

        if incident:
            self._load_incident(incident)

    def _load_incident(self, incident: Incident) -> None:
        self.title_edit.setText(incident.title)
        self.description_edit.setPlainText(incident.description)
        self.category_edit.setText(incident.category)
        self.assignee_edit.setText(incident.assignee)
        self.due_date_edit.setText(incident.due_date)
        self.tags_edit.setText(", ".join(incident.tags))
        self.priority_combo.setCurrentIndex(self.priority_combo.findData(incident.priority))
        self.status_combo.setCurrentIndex(self.status_combo.findData(incident.status))

    def payload(self) -> dict[str, object]:
        return {
            "title": self.title_edit.text(),
            "description": self.description_edit.toPlainText(),
            "category": self.category_edit.text(),
            "priority": self.priority_combo.currentData(),
            #¿como cojo la informacion del checbox con el valor que necesito?
            "status": self.status_combo.currentData(),
            "assignee": self.assignee_edit.text(),
            "due_date": self.due_date_edit.text(),
            "tags": [tag.strip() for tag in self.tags_edit.text().split(",")],
        }

