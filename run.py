from flask import Flask, render_template,request , redirect , flash , url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from flask_login import LoginManager,UserMixin,login_required,current_user,login_user,logout_user
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)


@app.route("/")
def index():
    data = Recipes.query.all()
    return render_template("HomePage.html")


@app.route("/Category")
def category():
    return render_template("category.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/sign")
def sign():
    return render_template("sign.html")



if __name__ == "__main__":
    app.run(debug=True)