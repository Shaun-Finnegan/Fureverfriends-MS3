from fureverfriends import db

# Customer Model


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    animals = db.relationship('Animal', backref="customer", lazy=True)

    def __repr__(self):
        return f"Customer('{self.first_name}'\
        '{self.last_name}','{self.email}')"
                           
# Animal Model


class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.String(50), nullable=False)
    animal_name = db.Column(db.String(50), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
   
    def __repr__(self):
        return f"Animal('{self.animal}', '{self.animal_name}')"
