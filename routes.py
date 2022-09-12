from app import app
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
from db import db


@app.route("/")
def index():
    sql = "SELECT selling_price, street_address FROM sold_apartment"
    result = db.session.execute(sql)
    apartments = result.fetchall()
    return render_template("index.html", count=len(apartments), apartments=apartments) 

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    #check username and passaword
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", name=request.form["username"])

@app.route("/create", methods=["POST"])
def send():
    street_address = request.form["street_address"]
    selling_price = request.form["selling_price"]
    sql = "INSERT INTO sold_apartment (street_address,selling_price) VALUES (:street_address,:selling_price)"
    db.session.execute(sql, {"street_address":street_address, "selling_price":selling_price})
    db.session.commit()
    return redirect("/")
