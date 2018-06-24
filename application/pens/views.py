from flask import render_template, request, url_for, redirect
from flask_login import login_required
from wtforms import Form

from application import app, db
from application.pens.models import Pen
from application.collections.models import Collection
from application.pens.forms import PenForm
from application.pens.forms import PenEditForm


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
    c = Collection.query.filter_by(pen_id=pen_id).delete()

    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("pens_index"))

@app.route("/pens/view/<pen_id>", methods=["GET"])
@login_required
def pen_view(pen_id):
    t = Pen.query.get(pen_id)
    form = PenForm()
    form.name.data = t.name
    form.country.data = t.country
    form.manufacturer.data = t.manufacturer
    return render_template("pens/view.html", pen = t, form = form)


#@app.route("/pens/edit", methods=["GET"])
#@login_required
#def pen_editForm():
#    
#    form = PenEditForm()
#    form.edit.choices = [(pen.id,pen.name) for pen in Pen.query.all()]
#    return render_template("pens/edit.html", form = form)



@app.route("/pens/edit/<pen_id>/", methods=["POST"])
@login_required
def pen_edit(pen_id):

    form = PenForm(request.form)
    p = Pen.query.get(pen_id)
    if not form.validate():
        return render_template("pens/view.html", form = form, pen = p)

    p.name = form.name.data
    p.manufacturer = form.manufacturer.data
    p.country = form.country.data
    db.session().commit()
    return redirect(url_for("pen_view", pen_id = pen_id))
    

