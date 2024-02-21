from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(40), index=True)
    lastname = db.Column(db.String(40))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return f'<User {self.firstname} {self.lastname}>'

    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email
        }
    
class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    homeworld = db.Column(db.Integer, db.ForeignKey('planet.id')) 
   
    def __repr__(self):
        return f'<Character name={self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "homeworld": self.homeworld,
        }


    
class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(40), unique=True)  # Añadir unique=True aquí
    climate = db.Column(db.String(40))
    rotation_period = db.Column(db.String(40))
    population = db.Column(db.String(40))
    
    def __repr__(self):
        return f'<Planet planet_name={self.planet_name}>'

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "climate": self.climate,
            "rotation_period": self.rotation_period,
            "population": self.population
        }


class favorite_planet(db.Model):
    __tablename__ = 'favorite_planet'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_name = db.Column(db.String(50), db.ForeignKey('planet.planet_name'))
    planet = db.relationship('Planet', foreign_keys=[planet_name], backref='favorite_planet')

    def __repr__(self):
        return f'<favorite_planet user_id={self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "name": self.planet.planet_name 
        }



class Vehicle(db.Model):
     __tablename__ = 'vehicle'
     id = db.Column(db.Integer, primary_key=True)
     vehicle_name = db.Column(db.String(40))
     model = db.Column(db.String(40))
     crew = db.Column(db.Integer)
     passengers = db.Column(db.Integer)

def __repr__(self):
        return f'<Vehicle vehicle_name={self.vehicle_name}>'

def serialize(self):
        return {
            "id": self.id,
            "vehicle_name": self.vehicle_name,
            "model": self.model,
            "crew": self.crew,
            "passengers": self.passengers
        }