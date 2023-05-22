from sqlalchemy.orm import Mapped, mapped_column

from app.models.db import BaseDatabase


class Restaurant(BaseDatabase):
    __tablename__ = "restaurant"
    name: Mapped[str] = mapped_column(unique=True)
