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
    role = request.form["role"]
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username, password, first_name, last_name, role) VALUES (:username, :password, :first_name, :last_name, :role)"
        db.session.execute(sql, {"username":username, "password":hash_value, "first_name":first_name, "last_name":last_name, "role":role})
        db.session.commit()
        return redirect("/")
    else:
        return render_template("error.html", message="Käyttäjätunnus on jo käytössä")


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/create", methods=["POST"])
def send():
    street_address = request.form["street_address"]
    apartment_number = request.form["apartment_number"]
    stairwell = request.form["stairwell"]
    zip_code = request.form["zip_code"]
    selling_price = request.form["selling_price"]
    squares_m2 = request.form["squares_m2"]
    housing_company_code = request.form["housing_company_code"]
    sales_date = request.form["sales_date"]
    # add user to the database automatically from the session

    sql = "INSERT INTO sold_apartment (street_address, apartment_number, stairwell, zip_code, selling_price, squares_m2, housing_company_code, sales_date) VALUES (:street_address,:apartment_number,:stairwell,:zip_code,:selling_price,:squares_m2,:housing_company_code,:sales_date)"
    db.session.execute(sql, {"street_address":street_address, "apartment_number":apartment_number, "stairwell":stairwell, "zip_code":zip_code, "selling_price":selling_price, "squares_m2":squares_m2, "housing_company_code":housing_company_code, "sales_date":sales_date})
    db.session.commit()
    return redirect("/")


@app.route("/new_housing_company")
def new_housing_company():
    return render_template("new_housing_company.html")


@app.route("/create_housing_company", methods=["POST"])
def create_housing_company():
    company_code = request.form["company_code"]
    street_address = request.form["street_address"]
    zip_code = request.form["zip_code"]
    construction_year = request.form["construction_year"]
    last_pipe_renovation_year = request.form["last_pipe_renovation_year"]

    sql = "SELECT company_code FROM housing_company WHERE company_code=:company_code"
    result = db.session.execute(sql, {"company_code":company_code})
    company = result.fetchone()
    if not company:
        
        sql = "INSERT INTO housing_company (company_code, street_address, zip_code, construction_year, last_pipe_renovation_year) VALUES (:company_code,:street_address,:zip_code,:construction_year,:last_pipe_renovation_year)"
        db.session.execute(sql, {"company_code":company_code, "street_address":street_address, "zip_code":zip_code, "construction_year":construction_year, "last_pipe_renovation_year":last_pipe_renovation_year})
        db.session.commit()
        return redirect("/")
    else:
        return render_template("error.html", message="Taloyhtiö on jo tietokannassa")


@app.route("/new_postal_area")
def new_postal_area():
    return render_template("new_postal_area.html")


@app.route("/create_postal_area", methods=["POST"])
def create_postal_area():
    zip_code = request.form["zip_code"]
    postal_area_name = request.form["postal_area_name"]
    municipality = request.form["municipality"]
    region = request.form["region"]
    country = request.form["country"]

    sql = "SELECT zip_code FROM postal_area WHERE zip_code=:zip_code"
    result = db.session.execute(sql, {"zip_code":zip_code})
    zip = result.fetchone()
    if not zip:
        sql = "INSERT INTO postal_area (zip_code, postal_area_name, municipality, region, country) VALUES (:zip_code,:postal_area_name,:municipality,:region,:country)"
        db.session.execute(sql, {"zip_code":zip_code, "postal_area_name":postal_area_name, "municipality":municipality, "region":region, "country":country})
        db.session.commit()
        return redirect("/")
    else:
        return render_template("error.html", message="Postinumeroalue on jo tietokannassa")

