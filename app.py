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


@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "cuisine_name": request.form.get("cuisine_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_serving": request.form.get("recipe_serving"),
            "recipe_time": request.form.get("recipe_time"),
            "food_category": request.form.get("food_category"),
            "age_range": request.form.get("age_range"),
            "img_url": request.form.get("img_url"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Added")
        return redirect(url_for("get_recipes"))

    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    categories = mongo.db.categories.find().sort("food_category", 1)
    ages = mongo.db.ages.find().sort("age_range", 1)
    return render_template("add_recipe.html", cuisines=cuisines, ages=ages,
                           categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "cuisine_name": request.form.get("cuisine_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_serving": request.form.get("recipe_serving"),
            "recipe_time": request.form.get("recipe_time"),
            "food_category": request.form.get("food_category"),
            "age_range": request.form.get("age_range"),
            "img_url": request.form.get("img_url"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
        }

        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Task Successfully Updated")
        return redirect(url_for("get_recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    categories = mongo.db.categories.find().sort("food_category", 1)
    ages = mongo.db.ages.find().sort("age_range", 1)
    return render_template("edit_recipe.html", recipe=recipe,
                           cuisines=cuisines, ages=ages, categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Task successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/view_recipe/<recipe_id>", methods=["GET"])
def view_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html", recipe=recipe)


@app.route("/shop_books")
def shop_books():
    return render_template("shop-books.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
