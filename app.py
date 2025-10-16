from flask import Flask, render_template, jsonify
from statistics import mean
from data import HOUSES

app = Flask(__name__)


@app.route("/")
def index():
    # Center map on the average lat/lon
    center = [
        mean([h["lat"] for h in HOUSES]),
        mean([h["lon"] for h in HOUSES]),
    ]
    return render_template("index.html", center=center)


@app.route("/data.json")
def data():
    return jsonify(HOUSES)


if __name__ == "__main__":
    # pip install flask
    app.run(debug=True)
