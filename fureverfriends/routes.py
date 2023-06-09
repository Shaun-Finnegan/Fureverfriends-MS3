from flask import render_template, request, redirect, url_for
from fureverfriends import app, db
from fureverfriends.models import Customer, Animal
from sqlalchemy import text

# Renders Home Page


@app.route('/')
def index():
    return render_template("index.html")

# Renders About Page


@app.route("/about")
def about():
    return render_template("about.html")

# Renders Animals Page


@app.route("/animals")
def animals():
    return render_template("animals.html")

# Renders booking Page


@app.route("/checklist", methods=["GET", "POST"])
def checklist():
    customers = Customer.query.all()
    animals = Animal.query.all()
    return render_template("checklist.html", customers=customers,
                           animals=animals)

# This shows that the information in the form has been sent to the database


@app.route("/success", methods=["GET", "POST"])
def success():
    if request.method == 'POST':
        customer = Customer(
            first_name=request.form.get('fname'),
            last_name=request.form.get('lname'),
            email=request.form.get('email'),
        )

        animal = Animal(
            animal=request.form.get('animal'),
            animal_name=request.form.get('animal_name'),
        )

        db.session.add(customer)
        db.session.commit()
        db.session.add(animal)
        db.session.commit()
        return redirect(url_for("checklist"))
    return render_template("success.html")

# This allows the user to edit the information they have submitted


@app.route("/edit/<int:id>",  methods=["GET", "POST"])
def edit(id):
    customer = Customer.query.get_or_404(id)

    if request.method == 'POST':
        customer.first_name = request.form.get('fname'),
        customer.last_name = request.form.get('lname'),
        customer.email = request.form.get('email'),
        db.session.commit()
        return redirect(url_for("checklist"))
    return render_template("edit.html", customer=customer)

# This allows the user to edit the animal information they have submitted


@app.route("/edit_animal/<int:animal_id>",  methods=["GET", "POST"])
def edit_animal(animal_id):
    animal = Animal.query.get_or_404(animal_id)

    if request.method == 'POST':
        animal.animal = request.form.get('animal'),
        animal.animal_name = request.form.get('animal_name'),
        db.session.commit()
        return redirect(url_for("checklist"))
    return render_template("edit_animal.html", animal=animal)


@app.route("/delete/<int:id>")
def delete(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for("checklist"))


@app.route("/delete_animal/<int:animal_id>")
def delete_animal(animal_id):
    animal = Animal.query.get_or_404(animal_id)
    db.session.delete(animal)
    db.session.commit()
    return redirect(url_for("checklist"))
