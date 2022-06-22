from flask_app import app
from flask import session, redirect, render_template, request, flash
from flask_app.models.dojos_model import Dojo
from flask_app.models.ninja_model import Ninja

# +++++++ FORM ROUTES +++++++


@app.route("/")
def show_dojos():
    all_dojos = Dojo.show_all_dojos()
    return render_template("dojos.html", all_dojos=all_dojos)


@app.route("/add_dojos", methods=['POST'])
def add_one_dojo():
    data = {
        'name': request.form['dojos_name']
    }
    Dojo.create_new_dojo(data)
    return redirect('/')


# +++++DISPLAY+++++++


@ app.route("/dojos_show/<int:dojo_id>")
def display_one_dojos(dojo_id):
    data = {
        "id": dojo_id
    }
    dojo = Dojo.get_one_dojo(data)
    ninjas = Ninja.get_dojo_for_ninja(data)
    return render_template('dojos_show.html', dojo=dojo, ninjas=ninjas)


@app.route("/ninjas/add")
def add_ninjas():
    all_dojos = Dojo.get_all_dojos()
    return render_template('ninjas.html', all_dojos=all_dojos)
