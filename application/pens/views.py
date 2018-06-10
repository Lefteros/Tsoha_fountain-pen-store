from flask import render_template, request, url_for, redirect
from flask_login import login_required

from application import app, db
from application.pens.models import Pen
from application.pens.forms import PenForm


@app.route("/pens/new/")
@login_required
def pen_form():
    return render_template("pens/new.html", form = PenForm())

    


@app.route("/pens", methods=["GET"])
@login_required
def pens_index():
    return render_template("pens/list.html", pen = Pen.query.all())




@app.route("/pens/", methods=["POST"])
@login_required
def pen_create():
    form = PenForm(request.form)

    if not form.validate():
        return render_template("pens/new.html", form = form)

    t = Pen(form.name.data)
    t.country = form.country.data
    t.manufacturer = form.manufacturer.data

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("pens_index"))


@app.route("/pens/delete/<pen_id>/", methods=["POST"])
@login_required
def pen_delete(pen_id):
    t = Pen.query.get(pen_id)

    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("pens_index"))
