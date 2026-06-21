import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SOURCE_DATA_DIR = BASE_DIR / "data"


def get_data_dir() -> Path:
    # Vercel functions can only write safely to /tmp at runtime.
    if os.getenv("VERCEL"):
        data_dir = Path("/tmp/project_web_data")
        data_dir.mkdir(parents=True, exist_ok=True)
        seed_runtime_data(data_dir)
        return data_dir

    SOURCE_DATA_DIR.mkdir(parents=True, exist_ok=True)
    return SOURCE_DATA_DIR


def seed_runtime_data(target_dir: Path) -> None:
    for source_file in SOURCE_DATA_DIR.glob("*"):
        if not source_file.is_file():
            continue

        target_file = target_dir / source_file.name
        if not target_file.exists():
            shutil.copy2(source_file, target_file)


def get_data_file(filename: str) -> Path:
    return get_data_dir() / filename
