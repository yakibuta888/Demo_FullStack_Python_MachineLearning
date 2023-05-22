from sqlalchemy.orm import Mapped, mapped_column

from app.models.db import BaseDatabase


class User(BaseDatabase):
    __tablename__ = "user"
    name: Mapped[str] = mapped_column(unique=True)
