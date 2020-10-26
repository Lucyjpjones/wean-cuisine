import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/homepage")
def homepage():
    return render_template("index.html")


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/add_recipe")
def add_recipe():
    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    categories = mongo.db.categories.find().sort("food_category", 1)
    ages = mongo.db.ages.find().sort("age_range", 1)
    return render_template("add_recipe.html", cuisines=cuisines, ages=ages,
                           categories=categories)


@app.route("/")
@app.route("/shop_books")
def shop_books():
    return render_template("shop-books.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
