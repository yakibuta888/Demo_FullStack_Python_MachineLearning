import datetime
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

import settings


class Base(DeclarativeBase):
    pass


class Database(object):
    def __init__(self) -> None:
        self.engine = create_engine(f"sqlite:///{settings.DB_NAME}")
        self.connect_db()

    def connect_db(self) -> Any:
        Base.metadata.create_all(self.engine)
        session = sessionmaker(self.engine)
        return session()


database = Database()


class BaseDatabase(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )
