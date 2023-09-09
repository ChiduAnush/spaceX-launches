from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


def fetch_spacex_launches():
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []


def categorize_launches(launches):
    successfull = list(filter(lambda x: x["success"] and not x["upcoming"], launches))
    failed = list(filter(lambda x: not x["success"] and not x["upcoming"], launches))
    upcoming = list(filter(lambda x: x["upcoming"], launches))

    return {"successfull": successfull, "failed": failed, "upcoming": upcoming}


launches = categorize_launches(fetch_spacex_launches())
print(launches)


if __name__ == "__main__":
    app.run(debug=True)
