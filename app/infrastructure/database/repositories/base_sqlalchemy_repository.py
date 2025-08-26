from abc import ABC
from sqlalchemy.orm import Session

from app import DatabaseDI


class BaseSqlAlchemyRepository(ABC):
    db_session: Session

    def __init__(self, session: DatabaseDI):
        self.db_session = session.session