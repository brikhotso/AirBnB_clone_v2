#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
import sqlalchemy


class City(BaseModel, Base):
    """Define City class """
    if models.is_type == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship('Place', backref='cities', cascade='all, delete')
    else:
        state_id = ""
        name = ""