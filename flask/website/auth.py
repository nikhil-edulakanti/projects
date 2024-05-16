from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_required,current_user

auth=Blueprint("auth",__name__)

@auth.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")

        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash("Logged in Succesfully!",category="success")
                login_user(user,remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password",category="error")
        else:
            flash("Email doesn't exits, Please signup", category="error")
    return render_template("login.html", user=current_user)

@auth.route("/signup",methods=["GET","POST"])
def sign_up():
    if request.method=="POST":
        email=request.form.get("email")
        firstName=request.form.get("firstName")
        password1=request.form.get("password1")
        password2=request.form.get("password2")
        
        user=User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists!",category="error")
        elif len(email)<4:
            flash("Email must be greater than 4 characters!",category="error")
        elif len(firstName)<2:
            flash("Firstname must be greater than 2 characters!",category="error")
        elif password1!=password2:
            flash("Passwords don't match",category="error")
        elif len(password1)<7:
            flash("Password should be greater than 7 characters",category="error")
        else:
            new_user=User(email=email,first_name=firstName,password=generate_password_hash(password1,method="pbkdf2:sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(user,remember=True)
            flash("Account created!", category="success")
            return redirect(url_for("views.home"))
    return render_template("sign-up.html",user=current_user)

@auth.route("/logout")
@login_required 
def logout():
    logout_user()
    return redirect(url_for("auth.login"))