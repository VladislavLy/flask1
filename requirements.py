from flask import Flask
from flask import render_template

the_app = Flask(__name__)


@the_app.route("/requirements")
@the_app.route("/")
def index():
    with open("templates/requirements.txt", "r") as f:
        text = f.readlines()

    return render_template("main.html", content = text)


if __name__ == "__main__":
    the_app.run(debug=True)




