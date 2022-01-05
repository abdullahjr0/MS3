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


@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        check = User.query.filter_by(email=email).first()
        if check:
            flash("Email Address already exists , try different one")
        else:
            try:
                user = User(
                    name=name,
                    email = email,
                    password = password
                )
                db.session.add(user)
                db.session.commit()
                login_user(user)
                flash('Register succesfully')
                return redirect('/profile')
            except:
                flash("Problem in Registration")
                return redirect("/register")
    return render_template("Sign-up.html")

@app.route("/login", methods=["GET","POST"])
def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            user = User.query.filter_by(email=email).first()
            try:
                if password == user.password:
                    login_user(user)
                    return redirect('/')
                else:
                    flash("Wrong password")
                    return redirect('/login')
            except:
                flash("Wrong Email Address")
                return redirect('/login')
        return render_template('/signin.html')

@app.route("/main_course")
def main_course():
    data = Recipes.query.filter_by(category='Main Course').all()
    return render_template("main_course.html", data=data)

@app.route("/drink")
def drink():
    data = Recipes.query.filter_by(category='Drink').all()
    return render_template("drink.html", data=data)


@app.route("/desert")
def desert():
    data = Recipes.query.filter_by(category="Desert").all()
    return render_template("desert.html",data=data)


@app.route("/contact")
@login_required
def contact():
    return render_template("FeedBackForm.html")

@app.route("/logout")
@login_required
    def logout():
    logout_user()
    return redirect("/")

@app.route("/contact_us", methods=["GET","POST"])
@login_required
def contact_us():
    message = "yes"
    return render_template("FeedBackForm.html", message = message)

if __name__ == "__main__":
    app.run(debug=True)