
from flask_app import app
from flask import redirect, render_template, request, session, flash
from flask_app.models.dojos_model import Dojo
from flask_app.models.ninja_model import Ninja


@app.route("/")
@app.route("/ninjas")
def show_ninjas():
    all_dojos = Dojo.show_all_dojos()
    return render_template("ninjas.html", all_dojos=all_dojos)


@app.route("/add_ninja", methods=['POST'])
def add_one_ninja():
    data = {
        'first_name': request.form['ninjas_first_name'],
        'last_name': request.form['ninjas_last_name'],
        'age': request.form['ninjas_age'],
        'dojo_id': request.form['dojo_id']
    }

    Ninja.create_one_ninja(data)
    return redirect("/")
