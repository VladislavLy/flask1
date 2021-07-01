import requests
from flask import Flask
from flask import render_template

the_app = Flask(__name__)


@the_app.route("/space/")
@the_app.route("/")
def index():
    responce = requests.get('http://api.open-notify.org/astros.json')
    result = responce.json()
    return render_template("space.html", content = result)


if __name__ == "__main__":
    the_app.run(debug=True)






