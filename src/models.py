import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))
    password = Column(String(250))

class DetalleCharacter(Base):
    __tablename__ = 'detalle_character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    species = Column(String(250))
    birth_year = Column(String(250))
    homeworld = Column(String(250))

class DetallesPlanets(Base):
    __tablename__ = 'detalles_planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(String(250))
    diameter = Column(Integer)
    terrain = Column(String(250))
    climate = Column(String(250))

class FavCharacter(Base):
    __tablename__ = 'fav_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('detalle_character.id'))
    relation_character = relationship("DetaleCharacter")
    relation_user = relationship("User")


class FavPlanets(Base):
    __tablename__ = 'fav_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('detalles_planets.id'))
    relation_planets = relationship("DetallesPlanets")
    relation_user = relationship("User")



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
