from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QSplitter,
    QTableView,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

from ..models import Incident, IncidentFilters, Priority, Status
from ..qt_models import IncidentTableModel
from ..services import IncidentService, IncidentValidationError
from .components import BadgeEstatIncidencia
from .dialogs import IncidentDialog


class MainWindow(QMainWindow):
    def __init__(self, service: IncidentService) -> None:
        super().__init__()
        self.service = service
        self.model = IncidentTableModel()
        self.table = QTableView()
        self.detail = QPlainTextEdit()
        self.search_edit = QLineEdit()
        self.status_filter = QComboBox()
        self.priority_filter = QComboBox()
        self.detail_badge = BadgeEstatIncidencia()

        self.setWindowTitle("Gestor d'incidencies")
        self._build_toolbar()
        self._build_body()
        self._connect_signals()
        self.refresh()

    def _build_toolbar(self) -> None:
        toolbar = QToolBar("Accions")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        add_action = toolbar.addAction("Nova")
        edit_action = toolbar.addAction("Editar")
        close_action = toolbar.addAction("Tancar")
        delete_action = toolbar.addAction("Eliminar")
        toolbar.addSeparator()
        reload_action = toolbar.addAction("Actualitzar")

        add_action.triggered.connect(self.create_incident)
        edit_action.triggered.connect(self.edit_selected)
        close_action.triggered.connect(self.close_selected)
        delete_action.triggered.connect(self.delete_selected)
        reload_action.triggered.connect(self.refresh)

    def _build_body(self) -> None:
        self.search_edit.setPlaceholderText("Cerca")
        self.status_filter.addItem("Tots els estats", None)
        self.priority_filter.addItem("Totes les prioritats", None)
        for status in Status:
            self.status_filter.addItem(status.value, status)
        for priority in Priority:
            self.priority_filter.addItem(priority.value, priority)

        filter_bar = QHBoxLayout()
        filter_bar.addWidget(QLabel("Text"))
        filter_bar.addWidget(self.search_edit, stretch=2)
        filter_bar.addWidget(QLabel("Estat"))
        filter_bar.addWidget(self.status_filter)
        filter_bar.addWidget(QLabel("Prioritat"))
        filter_bar.addWidget(self.priority_filter)
        clear_button = QPushButton("Netejar")
        clear_button.clicked.connect(self.clear_filters)
        filter_bar.addWidget(clear_button)

        self.table.setModel(self.model)
        self.table.setSelectionBehavior(QTableView.SelectRows)
        self.table.setSelectionMode(QTableView.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.detail_badge.hide()
        self.detail.setReadOnly(True)

        detail_layout = QVBoxLayout()
        detail_layout.addWidget(self.detail_badge, alignment=Qt.AlignLeft)
        detail_layout.addWidget(self.detail)
        detail_panel = QWidget()
        detail_panel.setLayout(detail_layout)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.table)
        splitter.addWidget(detail_panel)
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 2)

        layout = QVBoxLayout()
        layout.addLayout(filter_bar)
        layout.addWidget(splitter)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.statusBar().showMessage("Preparat")

    def _connect_signals(self) -> None:
        self.search_edit.textChanged.connect(self.refresh)
        self.status_filter.currentIndexChanged.connect(self.refresh)
        self.priority_filter.currentIndexChanged.connect(self.refresh)
        self.table.selectionModel().selectionChanged.connect(self.update_detail)
        self.table.doubleClicked.connect(self.edit_selected)

    def current_filters(self) -> IncidentFilters:
        return IncidentFilters(
            text=self.search_edit.text(),
            status=self.status_filter.currentData(),
            priority=self.priority_filter.currentData(),
        )

    def refresh(self) -> None:
        incidents = self.service.list_incidents(self.current_filters())
        self.model.update_incidents(incidents)
        self.statusBar().showMessage(f"{len(incidents)} incidencia/es visibles")
        self.update_detail()

    def clear_filters(self) -> None:
        self.search_edit.clear()
        self.status_filter.setCurrentIndex(0)
        self.priority_filter.setCurrentIndex(0)

    def selected_incident(self) -> Incident | None:
        indexes = self.table.selectionModel().selectedRows()
        if not indexes:
            return None
        return self.model.incident_at(indexes[0].row())

    def create_incident(self) -> None:
        dialog = IncidentDialog(self)
        if dialog.exec() != IncidentDialog.Accepted:
            return
        payload = dialog.payload()
        try:
            self.service.create_incident(
                title=str(payload["title"]),
                description=str(payload["description"]),
                category=str(payload["category"]),
                priority=payload["priority"],
                assignee=str(payload["assignee"]),
                due_date=str(payload["due_date"]),
                tags=payload["tags"],
            )
        except IncidentValidationError as exc:
            QMessageBox.warning(self, "Validacio", str(exc))
            return
        self.refresh()

    def edit_selected(self) -> None:
        incident = self.selected_incident()
        if not incident:
            QMessageBox.information(self, "Editar", "Selecciona una incidencia.")
            return
        dialog = IncidentDialog(self, incident)
        if dialog.exec() != IncidentDialog.Accepted:
            return
        try:
            self.service.update_incident(incident.id, **dialog.payload())
        except IncidentValidationError as exc:
            QMessageBox.warning(self, "Validacio", str(exc))
            return
        self.refresh()

    def close_selected(self) -> None:
        incident = self.selected_incident()
        if not incident:
            QMessageBox.information(self, "Tancar", "Selecciona una incidencia.")
            return
        self.service.close_incident(incident.id)
        self.refresh()

    def delete_selected(self) -> None:
        incident = self.selected_incident()
        if not incident:
            QMessageBox.information(self, "Eliminar", "Selecciona una incidencia.")
            return
        answer = QMessageBox.question(
            self,
            "Eliminar",
            f"Vols eliminar {incident.id}?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if answer != QMessageBox.Yes:
            return
        self.service.delete_incident(incident.id)
        self.refresh()

    def update_detail(self) -> None:
        incident = self.selected_incident()
        if not incident:
            self.detail_badge.hide()
            self.detail.setPlainText("")
            return
        self.detail_badge.set_estat(incident.status)
        self.detail_badge.show()
        self.detail.setPlainText(
            "\n".join(
                [
                    f"{incident.id} - {incident.title}",
                    f"Estat: {incident.status.value}",
                    f"Prioritat: {incident.priority.value}",
                    f"Categoria: {incident.category}",
                    f"Responsable: {incident.assignee or '-'}",
                    f"Venciment: {incident.due_date or '-'}",
                    f"Etiquetes: {', '.join(incident.tags) or '-'}",
                    "",
                    incident.description,
                ]
            )
        )
