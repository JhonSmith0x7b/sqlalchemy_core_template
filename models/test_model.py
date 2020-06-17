
import logging
from models.base_model import BaseModel


class TestModel(BaseModel):

    def __init__(self, id, name):
        self.id = id
        self.name = name
