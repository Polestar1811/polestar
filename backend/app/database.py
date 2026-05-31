from .mock_data import DB


def init_db() -> None:
    """MVP uses in-memory mock data; real persistence can replace this boundary."""
    DB.ensure_seeded()
