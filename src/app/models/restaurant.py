from sqlalchemy.orm import Mapped, mapped_column

from app.models.db import BaseDatabase, database


class Restaurant(BaseDatabase):
    __tablename__ = "restaurant"
    name: Mapped[str] = mapped_column(unique=True)

    @staticmethod
    def get(restaurant_id: int) -> "Restaurant | None":
        session = database.connect_db()
        row = session.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
        session.close()
        if row:
            return row
        return None

    @staticmethod
    def get_or_create(name: str) -> "Restaurant":
        session = database.connect_db()
        row = session.query(Restaurant).filter(Restaurant.name == name).first()
        if row:
            session.close()
            return row

        restaurant = Restaurant(name=name)
        session.add(restaurant)
        session.commit()

        row = session.query(Restaurant).filter(Restaurant.name == name).first()
        session.close()
        return row
