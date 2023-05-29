from flask import Flask, redirect, render_template, request, url_for

from app.controllers.forms import RateForm, YesOrNoForm
from app.models.user import User
from app.models.restaurant import Restaurant
from app.models.rate import Rate
import settings


app = Flask(__name__, template_folder=settings.TEMPLATE_FOLDER_PATH, static_folder=settings.STATIC_FOLDER_PATH)


class WebServer(object):
    def start(self, debug: bool = False) -> None:
        app.run(host="0.0.0.0", port=settings.PORT, debug=debug)


server: WebServer = WebServer()

ROBOT_NAME: str = 'Roboko'


def get_form2string(value: str) -> str:
    form_data: str | None = request.form.get(value, type=str)
    if form_data is not None:
        return form_data.strip()
    else:
        # TODO フォームで文字を入力するように促す
        raise ValueError


@app.route("/", methods=["GET", "POST"])
def hello() -> str:
    if request.method == "POST":
        user_name: str = get_form2string("user_name")
        user = User.get_or_create(user_name)
        restaurants = Rate.recommend_restaurant(user)
        if restaurants:
            form = YesOrNoForm(request.form)
            form.user_name.data = user_name
            return render_template("recommend_restaurant.html", user_name=user_name, restaurants=restaurants, form=form)

        form = RateForm(request.form)
        form.user_name.data = user_name
        return render_template("evaluate_restaurant.html", user_name=user_name, form=form)

    return render_template("hello.html", name=ROBOT_NAME)


@app.route("/restaurant/evaluate/status", methods=["GET", "POST"])
def evaluate_yes_or_no():
    if request.method == "POST":
        form = YesOrNoForm(request.form)
        user_name: str = form.user_name.data.strip()
        if form.value.data == "No":
            return render_template("good_by.html", user_name=user_name)

        form = RateForm(request.form)
        form.user_name.data = user_name
        return render_template("evaluate_restaurant.html", user_name=user_name, form=form)


@app.route("/restaurant/rate", methods=["GET", "POST"])
def restaurant_rate():
    form = RateForm(request.form)
    if request.method == "POST":
        user_name: str = form.user_name.data.strip()
        user: User = User.get_or_create(user_name)

        restaurant_name = form.restaurant.data.strip()
        restaurant: Restaurant = Restaurant.get_or_create(restaurant_name)

        value: int = int(form.rate.data)
        Rate.update_or_create(user, restaurant, value)

        return render_template("good_by.html", user_name=user_name)
