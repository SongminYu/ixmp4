from collections.abc import Generator
from pathlib import Path

from ixmp4.conf import settings

database_dir = settings.storage_directory / "databases"


def yield_databases() -> Generator[Path, None, None]:
    """Yields all local sqlite database files."""

    databases = database_dir.glob("*.sqlite3")
    return databases


def get_database_path(name: str) -> Path:
    """Returns a :class:`Path` object for a given sqlite database name.
    Does not check whether or not the file actually exists."""

    file_name = name + ".sqlite3"
    return database_dir / file_name


def get_dsn(database_path: Path) -> str:
    """Returns sqlalchemy-friendly sqlite database URI for a given database name."""

    return database_path.absolute().as_uri().replace("file://", "sqlite:///")


def search_databases(name: str) -> str | None:
    """Returns a database URI if the desired database exists, otherwise `None`."""

    database_path = get_database_path(name)
    return get_dsn(database_path) if database_path.exists() else None
