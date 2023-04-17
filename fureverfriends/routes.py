from flask import render_template, request, redirect, url_for
from fureverfriends import app, db
from fureverfriends.models import Customer
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
    return render_template("checklist.html", customers=customers)


@app.route("/success", methods=["GET", "POST"])
def success():
    if request.method == 'POST':
        customer = Customer(
            first_name=request.form.get('fname'),
            last_name=request.form.get('lname'),
            email=request.form.get('email'),
        )

        db.session.add(customer)
        db.session.commit()
    return render_template("index.html")


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


@app.route("/delete/<int:id>")
def delete(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for("checklist"))