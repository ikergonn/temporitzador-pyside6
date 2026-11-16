# El import relativo permite iniciar el proyecto con ``python -m prova.main``;
# el alternativo conserva la ejecucion directa de este archivo desde ``prova``.
from app import run


if __name__ == "__main__":
    raise SystemExit(run())

