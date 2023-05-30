import logging

import pandas as pd
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.schema import UniqueConstraint
from surprise import SVD, Dataset, NormalPredictor, Reader
from surprise.model_selection import cross_validate

import settings
from app.models.db import BaseDatabase, database
from app.models.restaurant import Restaurant
from app.models.user import User

logger = logging.getLogger(__name__)
TOP_RECOMMEND_RESTAURANT_NUM = 10


class Rate(BaseDatabase):
    __tablename__ = "rate"
    __table_args__ = (UniqueConstraint("user_id", "restaurant_id"),)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    restaurant_id: Mapped[int] = mapped_column(
        ForeignKey(Restaurant.id, ondelete="CASCADE")
    )
    value: Mapped[int]

    @staticmethod
    def update_or_create(user: User, restaurant: Restaurant, value: int) -> None:
        session = database.connect_db()
        rate = (
            session.query(Rate)
            .filter(Rate.user_id == user.id, Rate.restaurant_id == restaurant.id)
            .first()
        )
        if rate:
            rate.value = value
            session.commit()
            session.close()
        else:
            rate = Rate(user_id=user.id, restaurant_id=restaurant.id, value=value)
            session.add(rate)
            session.commit()
            session.close()

    @staticmethod
    def recommend_restaurant(user: User) -> list[str | None] | None:
        """
        Use machine learning to measure recommended restaurants and return the name of the recommended restaurant

        Parameters
        ----------
        user : User
            User object you want to recommend

        Returns
        -------
        list[str | None]
            A list of recommended restaurant names
        """
        if not settings.RECOMMEND_ENGINE_ENABLE:
            session = database.connect_db()
            recommend = [r.name for r in session.query(Restaurant).all()][
                :TOP_RECOMMEND_RESTAURANT_NUM
            ]
            session.close()
            return recommend

        session = database.connect_db()
        df = pd.read_sql("SELECT user_id, restaurant_id, value from rate", session.bind)
        session.close()

        dataset_columns = ["user_id", "restaurant_id", "value"]
        reader = Reader()
        data = Dataset.load_from_df(df[dataset_columns], reader)
        try:
            cross_validate(NormalPredictor(), data, cv=2)
        except ValueError as ex:
            logger.error({"action": "recommend_restaurant", "error": ex})
            return None

        svd = SVD()
        trainset = data.build_full_trainset()
        svd.fit(trainset)

        predict_df = df.copy()
        item_id = "restaurant_id"
        predict_df["Predicted_Score"] = predict_df[item_id].apply(
            lambda x: svd.predict(user.id, x).est
        )
        predict_df = predict_df.sort_values(by=["Predicted_Score"], ascending=False)
        predict_df = predict_df.drop_duplicates(subset=item_id)

        if predict_df is None:
            logger.warning(
                {"action": "recommend_restaurant", "status": "no predict data"}
            )
            return []

        recommend_restaurants: list[str | None] = []
        for index, row in predict_df.iterrows():
            restaurant_id: int = int(row["restaurant_id"])
            restaurant: Restaurant | None = Restaurant.get(restaurant_id)
            recommend_restaurants.append(restaurant.name)

        return recommend_restaurants[:TOP_RECOMMEND_RESTAURANT_NUM]
