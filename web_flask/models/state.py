#!/usr/bin/python3
"""Defines the State class."""
"""Defines the State class."""
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from models import storage

class State(BaseModel, Base):
    """Represents a state for a MySQL database."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_STORAGE_TYPE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Get a list of City instances with state_id equals to the current State.id."""
            return [city for city in storage.all(City).values() if city.state_id == self.id]

