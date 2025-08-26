from dataclasses import dataclass

from app.infrastructure.database.session import get_db

@dataclass
class DatabaseDI:
    @property
    def session(self):
        return get_db()
