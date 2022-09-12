from crypt import methods
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
    #check username and password
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return render_template("error.html", message="Tunnusta ei löydy")
    else: 
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["username"] = username
            return redirect("/")
        else:
            return render_template("error.html", message="Salasana on väärä")
    

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/register", methods=["POST"])
def register():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    username = request.form["username"]
    password = request.form["password"]
    #check that no user with this username
    hash_value = generate_password_hash(password)
    sql = "INSERT INTO users (username, password, first_name, last_name) VALUES (:username, :password, :first_name, :last_name)"
    db.session.execute(sql, {"username":username, "password":hash_value, "first_name":first_name, "last_name":last_name})
    db.session.commit()
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
