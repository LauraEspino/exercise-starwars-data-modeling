import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password=Column(String(250), nullable=False)
    characters_favorite=Column(String(250), nullable=False)
    planet_favorite=Column(String(250), nullable=False)
    vehicle_favorite=Column(String(250), nullable=False)
    characters=relationship('Favorites_Characters', backref='user', lazy=True)
    planets=relationship('Favorites_Planets', backref='user', lazy=True)
    vehicles=relationship('Favorites_Vehicles', backref='user', lazy=True)
    

class Favorites_Characters(Base):
    # id:Column(Integer, primary_key=True)
    __tablename__="favorites_characters"
    id = Column(Integer, primary_key=True)
    id_user=Column(Integer,ForeignKey('user.id'),nullable=False)
    characters=relationship('Characters', backref='favorites_characters', lazy=True)

class Favorites_Planets(Base):
    # id:Column(Integer, primary_key=True)
    __tablename__="favorites_planets"
    id = Column(Integer, primary_key=True)
    id_user=Column(Integer,ForeignKey('user.id'),nullable=False)
    planets=relationship('Planet', backref='favorites_planets', lazy=True)

class Favorites_Vehicles(Base):
    # id:Column(Integer, primary_key=True)
    __tablename__="favorites_vehicles"
    id = Column(Integer, primary_key=True)
    id_user=Column(Integer,ForeignKey('user.id'),nullable=False)
    vehicles=relationship('Vehicles', backref='favorites_vehicles', lazy=True)


    def to_dict(self):
        return {}

class Characters(Base):
    # id:Column(Integer, primary_key=True)
    __tablename__="characters"
    id = Column(Integer, primary_key=True)
    birth_year= Column(String(250), nullable=False)
    eye_color=Column(String(250), nullable=False)
    films=Column(String(250), nullable=False) 
    gender=Column(String(250), nullable=False) 
    hair_color=Column(String(250), nullable=False) 
    height=Column(Integer, nullable=False) 
    homeworld=Column(String(250), nullable=False)
    mass=Column(Integer, nullable=False) 
    name=Column(String(250), nullable=False)
    skin_color=Column(String(250), nullable=False)
    starships=Column(String(250), nullable=False)
    vehicles=Column(String(250), nullable=False)
    id_favorites_characters=Column(Integer,ForeignKey('favorites_characters.id'),nullable=False)

    def to_dict(self):
        return {}
    
class Planet(Base):
    __tablename__="planets"
    id = Column(Integer, primary_key=True)
    climate=Column(String(250), nullable=False)
    diameter=Column(Integer, nullable=False)
    gravity=Column(Integer, nullable=False)
    name=Column(String(250), nullable=False)
    population=Column(Integer, nullable=False)
    rotation_period=Column(Integer, nullable=False)
    terrain=Column(String(250), nullable=False)
    id_favorites_planets=Column(Integer,ForeignKey('favorites_planets.id'),nullable=False)
    
    def to_dict(self):
        return {}
    
class Vehicles(Base):
    # id:Column(Integer, primary_key=True)
    __tablename__="vehicles"
    id = Column(Integer, primary_key=True)
    cargo_capacity=Column(Integer, nullable=False)
    crew=Column(Integer, nullable=False)
    length=Column(Integer, nullable=False)
    model=Column(String(250), nullable=False)
    name=Column(String(250), nullable=False)
    passengers=Column(Integer, nullable=False)
    id_favorites_vehicles=Column(Integer,ForeignKey('favorites_vehicles.id'),nullable=False)

    def to_dict(self):
        return {}
    



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
