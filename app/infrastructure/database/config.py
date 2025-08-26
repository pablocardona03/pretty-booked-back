import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

Base = declarative_base(metadata=MetaData(naming_convention=naming_convention))

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)

SessionLocal = scoped_session(
    sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)
)

def init_db():
    Base.metadata.create_all(bind=engine)