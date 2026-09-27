from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def caminho_projeto(caminho_relativo: str) -> Path:
    """Retorna o caminho absoluto de um arquivo dentro do projeto."""
    return BASE_DIR / caminho_relativo
