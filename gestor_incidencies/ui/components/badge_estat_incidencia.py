from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QLabel, QWidget

from ...models import Status


class BadgeEstatIncidencia(QLabel):
    """Etiqueta reutilitzable per mostrar l'estat d'una incidencia."""

    estat_canviat = Signal(str)
    clicat = Signal(str)

    _LABELS = {
        Status.OPEN.value: "Oberta",
        Status.IN_PROGRESS.value: "En proces",
        Status.BLOCKED.value: "Bloquejada",
        Status.CLOSED.value: "Tancada",
    }

    _STYLES = {
        Status.OPEN.value: ("#1d4ed8", "#dbeafe"),
        Status.IN_PROGRESS.value: ("#92400e", "#fef3c7"),
        Status.BLOCKED.value: ("#991b1b", "#fee2e2"),
        Status.CLOSED.value: ("#166534", "#dcfce7"),
    }

    def __init__(self, estat: Status | str = Status.OPEN, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._estat = Status.OPEN.value
        self.setObjectName("badgeEstatIncidencia")
        self.setAlignment(Qt.AlignCenter)
        self.setMinimumWidth(88)
        self.setCursor(Qt.PointingHandCursor)
        self.set_estat(estat, emit=False)

    def get_estat(self) -> str:
        return self._estat

    def set_estat(self, estat: Status | str, *, emit: bool = True) -> None:
        normalized = self._normalize_estat(estat)
        changed = normalized != self._estat
        self._estat = normalized
        self.setText(self._LABELS[normalized])
        self.setToolTip(f"Estat de la incidencia: {self._LABELS[normalized]}")
        self.setProperty("estat", normalized)
        self.setStyleSheet(self._style_for(normalized))
        if changed and emit:
            self.estat_canviat.emit(normalized)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.clicat.emit(self._estat)
        super().mousePressEvent(event)

    @classmethod
    def _normalize_estat(cls, estat: Status | str) -> str:
        value = estat.value if isinstance(estat, Status) else str(estat)
        if value not in cls._LABELS:
            valid = ", ".join(cls._LABELS)
            raise ValueError(f"Estat d'incidencia no valid: {value}. Valors valids: {valid}")
        return value

    @classmethod
    def _style_for(cls, estat: str) -> str:
        foreground, background = cls._STYLES[estat]
        return (
            "QLabel#badgeEstatIncidencia {"
            f"color: {foreground};"
            f"background-color: {background};"
            "border: 1px solid rgba(0, 0, 0, 0.12);"
            "border-radius: 6px;"
            "padding: 4px 8px;"
            "font-weight: 600;"
            "}"
        )
