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


# Homepage function
@app.route("/")
@app.route("/homepage")
def homepage():
    """
    Finds all the cuisines in the db and sorts them by cuisine name
    to display alphabetically in carousel.
    """
    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    return render_template("index.html", cuisines=cuisines)


# Recipes page function
@app.route("/get_recipes")
def get_recipes():
    """
    Finds all the recipes in the db and sorts the cards
    alphabetically by recipe name.
    """
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    return render_template("recipes.html", recipes=recipes)


# Search bar function
@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Performs text index search on the recipes
    collection using the query variable.
    """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# Register modal function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        """Check if the username already exists in db"""
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists, please log in")
            return redirect(url_for("register"))
        else:
            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.insert_one(register)

            """Put the new user into 'session' cookie"""
            session["user"] = request.form.get("username").lower()
            flash("Registration successful, welcome {}".format(
                request.form.get("username")))
            return redirect(url_for("homepage", username=session["user"]))

    return redirect(url_for("homepage"))


# Login modal function
@app.route("/login", methods=["GET", "POST"])
def login():
    """Check if the username exists in db"""
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            """Ensure the hashed password matches the users input"""
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("{} successfully logged in".format(
                    request.form.get("username")))
                return redirect(url_for("homepage", username=session["user"]))

            else:
                """Invalid password match"""
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            """Username doesn't exist"""
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return redirect(url_for("homepage"))


# Logout function
@app.route("/logout")
def logout():
    """Remove user from session cookie"""
    session.pop("user")
    flash("Successfully logged out")
    return redirect(url_for("login"))


# Add recipe function
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    If post method is executed, create a dictionary for form
    and insert user input into the db
    """
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
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        return redirect(url_for("get_recipes"))

    """Sort form values in alphabetical order"""
    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    categories = mongo.db.categories.find().sort("food_category", 1)
    ages = mongo.db.ages.find().sort("_id", 1)
    return render_template("add_recipe.html", cuisines=cuisines, ages=ages,
                           categories=categories)


# Edit recipe function
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    If post method is executed, find recipe by id
    and update db with new form input
    """
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
            "created_by": session["user"]
        }

        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        return redirect(url_for("get_recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    categories = mongo.db.categories.find().sort("food_category", 1)
    ages = mongo.db.ages.find().sort("_id", 1)
    return render_template("edit_recipe.html", recipe=recipe,
                           cuisines=cuisines, ages=ages, categories=categories)


# Delete recipe function
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """Find recipe by id and remove from the db"""
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for("get_recipes"))


# View recipe information function
@app.route("/view_recipe/<recipe_id>", methods=["GET"])
def view_recipe(recipe_id):
    """Find recipe by id and direct to view recipe page"""
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html", recipe=recipe)


# Cuisines page function
@app.route("/get_cuisines")
def get_cuisines():
    """
    Direct to cuisine page with cuisine cards sorted
    alphabetically by cuisine name
    """
    cuisines = mongo.db.cuisines.find().sort("cuisine_name", 1)
    return render_template("cuisines.html", cuisines=cuisines)


# Add cuisine function
@app.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    """
    If post method is executed, find cuisine by id
    and update db with new form input
    """
    if request.method == "POST":
        cuisine = {
            "cuisine_name": request.form.get("cuisine_name"),
            "img_url": request.form.get("img_url")
        }
        mongo.db.cuisines.insert_one(cuisine)
        return redirect(url_for("get_cuisines"))

    return render_template("add_cuisine.html")


# Edit cuisine function
@app.route("/edit_cuisine/<cuisine_id>", methods=["GET", "POST"])
def edit_cuisine(cuisine_id):
    """
    If post method is executed, find cuisine by id
    and update db with new form input
    """
    if request.method == "POST":
        submit = {
            "cuisine_name": request.form.get("cuisine_name"),
            "img_url": request.form.get("img_url")
        }
        mongo.db.cuisines.update({"_id": ObjectId(cuisine_id)}, submit)
        return redirect(url_for("get_cuisines"))

    cuisine = mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)})
    return render_template("edit_cuisine.html", cuisine=cuisine)


# Delete cuisine function
@app.route("/delete_cuisine/<cuisine_id>")
def delete_cuisine(cuisine_id):
    """Find cuisine by id and remove from db"""
    mongo.db.cuisines.remove({"_id": ObjectId(cuisine_id)})
    return redirect(url_for("get_cuisines"))


# Filter recipes by cuisine function
@app.route("/filter_cuisine/<cuisine_name>", methods=["GET", "POST"])
def filter_cuisine(cuisine_name):
    """Direct to recipes page filted by the cuisine name selected by user"""
    recipes = list(mongo.db.recipes.find(
        {"cuisine_name": cuisine_name}))
    return render_template("recipes.html", recipes=recipes)


# Shop recipe books function
@app.route("/shop_books")
def shop_books():
    return render_template("shop-books.html")


# 404 page function
# Code from 'https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/'
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
