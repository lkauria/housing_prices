from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/in", methods=["POST"])
def result():
    return render_template("in.html")