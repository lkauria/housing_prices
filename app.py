from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///housing"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute("SELECT selling_price FROM sold_apartment")
    apartments = result.fetchall()
    return render_template("index.html", count=len(apartments), apartments=apartments) 

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", name=request.form["username"])

@app.route("/send", methods=["POST"])
def send():
    street_address = request.form["street_address"]
    selling_price = request.form["selling_price"]
    print("asunnon tiedot tuli tänne, mutta niiden tallentaminen ei ole vielä tehty")
    sql = "INSERT INTO sold_apartment (street_address,selling_price) VALUES (:street_address,:selling_price)"
    db.session.execute(sql, {"street_address":street_address, "selling_price":selling_price})
    db.session.commit()
    return redirect("/")
