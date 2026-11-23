"""Punto de entrada ejecutable desde la carpeta de la aplicacion."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__:
    from .app import run
else:
    # Al ejecutar ``python main.py``, Python no conoce todavia el paquete
    # ``gestor_incidencies``. Anadir su carpeta contenedora permite conservar
    # los imports relativos del resto de la aplicacion.
    package_parent = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(package_parent))
    from gestor_incidencies.app import run


if __name__ == "__main__":
    raise SystemExit(run())

