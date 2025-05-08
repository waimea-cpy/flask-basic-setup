from flask import Flask
from flask import render_template

# Create the app
app = Flask(__name__)


# -------------------------------------------------------
# Home page route
@app.get("/")
def hello():
    return render_template("pages/home.jinja")


# -------------------------------------------------------
# About page route
@app.get("/about")
def about():
    return render_template("pages/about.jinja")

