from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox,QAbstractItemView, QHeaderView

from PySide6.QtGui import QStandardItemModel, QStandardItem

from pathlib import Path

ruta_css = Path(__file__).with_name("prova.qss")
css = ruta_css.read_text(encoding="utf-8")


# Al ejecutar como modulo se necesita un import relativo; al ejecutar este
# archivo directamente, ``__package__`` es vacio y se usa el import local.
if __package__:
    from .interactions import connect_button_prints
    from .ui.prova import Ui_MainWindow
else:
    from interactions import connect_button_prints
    from ui.prova import Ui_MainWindow

def project_root() -> Path:
    return Path(__file__).resolve().parent


# Ui_MainWindow solo describe y construye los widgets: no es una ventana y no
# tiene ``show()``. Esta clase aporta el QMainWindow que debe mostrarse.
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        connect_button_prints(self.ui)
 # Conectar las acciones de los menús
        self.ui.actionAbrir.triggered.connect(self.abrir)
        self.ui.actionCerrar.triggered.connect(self.close)
        self.ui.actionadios.triggered.connect(self.adios)
        self.ui.action12.triggered.connect(self.num)
        self.ui.tableView.setStyleSheet(css)

        # 1. Crear el modelo
        self.modelo = QStandardItemModel(self)

        # 2. Definir las columnas
        self.modelo.setHorizontalHeaderLabels(
            ["Nombre", "Curso", "Nota"]
        )

        # 3. Preparar los datos
        alumnos = [
            ["Ana García", "DAM1", "8.5"],
            ["Pedro López", "DAM2", "7.2"],
            ["Marta Ruiz", "DAM1", "9.1"],
            ["Luis Pérez", "DAM2", "6.8"]
        ]

        # 4. Añadir filas al modelo
        for alumno in alumnos:
            fila = [
                QStandardItem(valor) for valor in alumno
            ]
            self.modelo.appendRow(fila)

        # 5. Asociar el modelo a la tabla
        tabla = self.ui.tableView
        tabla.setModel(self.modelo)

        # 6. Ajustar las columnas al ancho disponible
        tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        # 7. Seleccionar filas completas
        tabla.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        # 8. Impedir la edición directa
        tabla.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        # 9. Colores alternos por fila
        tabla.setAlternatingRowColors(True)



    def nuevo(self):
        QMessageBox.information(
            self, "Nuevo", "Crear un documento nuevo"
        )

    def abrir(self):
        QMessageBox.information(
            self, "Abrir", "Abrir un documento"
        )
    def close(self):
        QMessageBox.information(
            self, "Cerrar", "Cerrar un documento"
        )
    def adios(self):
         QMessageBox.information(
            self, "adios", "lol"
        )
    def num(self):
        QMessageBox.information(
            self, "12", "informacion"
        )
def create_main_window(data_path: Path | None = None) -> MainWindow:
    return MainWindow()


def run(argv: list[str] | None = None) -> int:
    app = QApplication(argv or sys.argv)
    window = create_main_window()
    window.resize(1080, 680)
    window.show()
    return app.exec()

