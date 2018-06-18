from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import RegisterForm
from application.collections.models import Collection

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)


    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    
    
    login_user(user)
    return redirect(url_for("index"))    


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))    

@app.route("/auth/create", methods = ["GET"])
def auth_form():
    return render_template("auth/new.html", form = RegisterForm())

@app.route("/auth/", methods = ["POST"])
def auth_create():
    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    u = User(form.name.data, form.username.data, form.password.data)

    db.session().add(u)
    db.session().commit()
    
    return redirect(url_for("auth_login"))

@app.route("/auth/list", methods = ["GET"])
@login_required
def auth_list():
    admin = current_user.admin
    return render_template("auth/list.html", users=User.get_users_and_pennro(), admin = admin)

@app.route("/user/<user_id>", methods=["POST"])
@login_required
def auth_delete(user_id):
    u = User.query.get(user_id)
#    c = Collection.query.filter_by(account_id=user_id).all
#    db.session().delete(c)
    db.session().delete(u)
    db.session().commit()

    return redirect(url_for("auth_list"))





