from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project0.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/employment")
def employment():
    return render_template("employment.html")

@app.route("/personalinfo")
def personalinfo():
    return render_template("personalInfo.html")

@app.route("/search", methods=['POST'])
def search():
    query = request.form.get("query")
    return redirect(f"https://www.google.com/search?q={query}")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/BS4utilities")
def BS4Utilities():
    return render_template("utilities.html")

@app.route("/BS4flex")
def BS4Flex():
    return render_template("flex.html")