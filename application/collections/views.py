from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from wtforms import Form

from application import app, db

from application.collections.models import Collection

from application.collections.forms import CollectionForm
from application.collections.forms import CollectionEditForm

from application.pens.models import Pen


@app.route("/collection/", methods=["GET"])
@login_required
def collection_index():

    form = CollectionForm()
    form.pen.choices = [(pen.id,pen.name) for pen in Pen.query.all()]

    return render_template("collections/list.html", collection = Collection.query.filter_by(account_id=current_user.id).all(), form = form)


@app.route("/collection/", methods=["POST"])
@login_required
def collection_add():

    form = CollectionForm(request.form)
    form.pen.choices = [(pen.id,pen.name) for pen in Pen.query.all()]

    if not form.validate():

        return render_template("collections/list.html", collection = Collection.query.filter_by(account_id=current_user.id).all(), form = form)

    c = Collection(form.pen.data)
    c.nib = form.nib.data
    c.color = form.color.data
    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("collection_index"))


@app.route("/collection/delete/<collection_id>/", methods=["POST"])
@login_required
def collection_delete(collection_id):

    c = Collection.query.get(collection_id)

    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("collection_index"))


@app.route("/collection/view/<collection_id>", methods=["GET"])
@login_required
def collection_view(collection_id):

    c = Collection.query.get(collection_id)
    form = CollectionEditForm()
    form.nib.data = c.nib
    form.color.data = c.color

    return render_template("collections/view.html", collection = c, form=form)


@app.route("/collection/edit/<collection_id>/", methods=["POST"])
@login_required
def collection_edit(collection_id):

    form = CollectionEditForm(request.form)

    if not form.validate():

        return render_template("collections/view.html", form = form, collection = Collection.query.get(collection_id))

    c = Collection.query.get(collection_id)
    c.nib = form.nib.data
    c.color = form.color.data

    db.session().commit()

    return redirect(url_for("collection_view", collection_id = collection_id))


