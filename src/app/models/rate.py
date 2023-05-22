from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.schema import UniqueConstraint

from app.models.db import BaseDatabase
from app.models.user import User
from app.models.restaurant import Restaurant


class Rate(BaseDatabase):
    __tablename__ = "rate"
    __table_args__ = (
        UniqueConstraint("user_id", "restaurant_id"),
    )
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    restaurant_id: Mapped[int] = mapped_column(ForeignKey(Restaurant.id, ondelete="CASCADE"))
    value: Mapped[int]
