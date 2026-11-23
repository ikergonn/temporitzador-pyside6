from __future__ import annotations

try:
    from PySide6.QtCore import Qt

    from gestor_incidencies.models import Status
    from gestor_incidencies.ui.components import BadgeEstatIncidencia
except ModuleNotFoundError as exc:  # pragma: no cover - executed only without GUI deps
    Qt = None
    Status = None
    BadgeEstatIncidencia = None
    _IMPORT_ERROR = exc
else:
    _IMPORT_ERROR = None


def _require_gui_dependencies() -> None:
    if _IMPORT_ERROR is not None:
        import pytest

        pytest.skip(f"Dependencia GUI no disponible: {_IMPORT_ERROR}")


def test_badge_te_estat_per_defecte(qtbot) -> None:
    _require_gui_dependencies()
    badge = BadgeEstatIncidencia()
    qtbot.addWidget(badge)

    assert badge.get_estat() == Status.OPEN.value
    assert badge.text() == "Oberta"
    assert badge.property("estat") == Status.OPEN.value


def test_badge_canvia_estat_i_emet_senyal(qtbot) -> None:
    _require_gui_dependencies()
    badge = BadgeEstatIncidencia()
    qtbot.addWidget(badge)

    with qtbot.waitSignal(badge.estat_canviat) as blocker:
        badge.set_estat(Status.IN_PROGRESS)

    assert blocker.args == [Status.IN_PROGRESS.value]
    assert badge.get_estat() == Status.IN_PROGRESS.value
    assert badge.text() == "En proces"


def test_badge_rebutja_estat_no_valid(qtbot) -> None:
    _require_gui_dependencies()
    badge = BadgeEstatIncidencia()
    qtbot.addWidget(badge)

    try:
        badge.set_estat("arxivada")
    except ValueError:
        pass
    else:
        raise AssertionError("BadgeEstatIncidencia hauria de rebutjar un estat no valid")


def test_badge_emet_senyal_en_clic(qtbot) -> None:
    _require_gui_dependencies()
    badge = BadgeEstatIncidencia(Status.CLOSED)
    qtbot.addWidget(badge)
    badge.show()

    with qtbot.waitSignal(badge.clicat) as blocker:
        qtbot.mouseClick(badge, Qt.LeftButton)

    assert blocker.args == [Status.CLOSED.value]
