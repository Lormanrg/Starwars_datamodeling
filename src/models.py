import enum
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

    def created(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

class Characters(Base):
    __tablename__="characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(String(50), nullable=False)
    mass = Column(String(50), nullable=False)
    def speak():
        return{}
    def fight():
        return{}


class Nature(enum.Enum):
    planets = "planets"
    characters = "characters"

class Favorites(Base):
    __tablename__ = "Favorites"
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer, nullable=False)
    nature_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    nature = Column("nature",Enum(Nature))
    
    def add_favorites():
        return {}



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
