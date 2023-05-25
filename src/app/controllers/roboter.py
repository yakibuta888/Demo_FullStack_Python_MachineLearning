from flask import Flask, redirect, render_template, request, url_for

import settings


app = Flask(__name__, template_folder=settings.TEMPLATE_FOLDER_PATH, static_folder=settings.STATIC_FOLDER_PATH)


class WebServer(object):
    def start(self, debug: bool = False) -> None:
        app.run(host="0.0.0.0", port=settings.PORT, debug=debug)


server: WebServer = WebServer()

ROBOT_NAME: str = 'Roboko'


@app.route("/", methods=["GET", "POST"])
def hello() -> str:
    if request.method == "POST":
        user_name: str = request.form.get("user_name", type=str).strip()
        return render_template("evaluate_restaurant.html", user_name=user_name)

    return render_template("hello.html", name=ROBOT_NAME)
