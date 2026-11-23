from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from .repository import JsonIncidentRepository
from .services import IncidentService
#from .ui.main_window import MainWindow
from .ui.main_window import MainWindow

def project_root() -> Path:
    """Carpeta autocontenida de la aplicacion."""
    return Path(__file__).resolve().parent


def create_main_window(data_path: Path | None = None) -> MainWindow:
    root = project_root()
    seed_path = root / "resources" / "incidents_seed.json"
    repository = JsonIncidentRepository(data_path or root / "data" / "incidents.json", seed_path)
    service = IncidentService(repository)
    return MainWindow(service)


def run(argv: list[str] | None = None) -> int:
    app = QApplication(argv or sys.argv)
    window = create_main_window()
    window.resize(1080, 680)
    window.show()
    return app.exec()

