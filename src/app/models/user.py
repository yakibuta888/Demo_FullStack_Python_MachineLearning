from sqlalchemy.orm import Mapped, mapped_column

from app.models.db import BaseDatabase, database


class User(BaseDatabase):
    __tablename__ = "user"
    name: Mapped[str] = mapped_column(unique=True)

    @staticmethod
    def get_or_create(name: str) -> "User":
        session = database.connect_db()
        row = session.query(User).filter(User.name == name).first()
        if row:
            session.close()
            return row

        user = User(name=name)
        session.add(user)
        session.commit()

        row = session.query(User).filter(User.name == name).first()
        session.close()
        return row
