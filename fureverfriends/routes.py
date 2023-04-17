from flask import render_template, request, redirect, url_for
from fureverfriends import app, db
from fureverfriends.models import Customer, Animal
from sqlalchemy import text


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/animals")
def animals():
    return render_template("animals.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/checklist", methods=["GET", "POST"])
def checklist():
    customers = Customer.query.all()
    animals = Animal.query.all()
    return render_template("checklist.html", customers=customers, animals=animals)


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

        db.session.add(customer, animal)
        db.session.commit()
    return render_template("success.html")





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


@app.route("/edit_animal/<int:id>",  methods=["GET", "POST"])
def edit_animal(id):
    animal = Animal.query.get_or_404(id)
 
    if request.method == 'POST':
        animal.animal = request.form.get('animal'),
        customer.animal_name = request.form.get('animal_name'),
        
        db.session.commit()
        return redirect(url_for("checklist"))  
    return render_template("edit.html", animal=animal)


@app.route("/delete/<int:id>")
def delete(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for("checklist"))


@app.route("/delete_animal/<int:id>")
def delete_animal(id):
    animal = Animal.query.get_or_404(id)
    db.session.delete(animal)
    db.session.commit()
    return redirect(url_for("checklist"))

