from __future__ import annotations

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from .models import Incident


class IncidentTableModel(QAbstractTableModel):
    HEADERS = ["Id", "Titol", "Categoria", "Prioritat", "Estat", "Responsable", "Venciment"]

    def __init__(self, incidents: list[Incident] | None = None) -> None:
        super().__init__()
        self._incidents = incidents or []

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        if parent.isValid():
            return 0
        return len(self._incidents)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        if parent.isValid():
            return 0
        return len(self.HEADERS)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> object:
        if not index.isValid() or role not in (Qt.DisplayRole, Qt.ToolTipRole):
            return None
        incident = self._incidents[index.row()]
        values = [
            incident.id,
            incident.title,
            incident.category,
            incident.priority.value,
            incident.status.value,
            incident.assignee,
            incident.due_date,
        ]
        return values[index.column()]

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.DisplayRole,
    ) -> object:
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.HEADERS[section]
        return section + 1

    def update_incidents(self, incidents: list[Incident]) -> None:
        self.beginResetModel()
        self._incidents = incidents
        self.endResetModel()

    def incident_at(self, row: int) -> Incident | None:
        if row < 0 or row >= len(self._incidents):
            return None
        return self._incidents[row]

