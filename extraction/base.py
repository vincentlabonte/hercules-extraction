import pathlib
from enum import Enum

class EntityExtractor():
    def extract_entity(self, text):
        pass

class EntityType(Enum):
    UNKNOWN	= 0
    PERSON = 1
    LOCATION = 2
    ORGANIZATION = 3
    EVENT = 4
    WORK_OF_ART = 5
    CONSUMER_GOOD = 6
    OTHER = 7
    PHONE_NUMBER = 8
    ADDRESS = 9
    DATE = 10
    NUMBER = 11
    PRICE = 12

class Entity():
    def __init__(self, name, entity_type):
        self.name = name
        self.entity_type = entity_type
    
    def __str__(self):
        return f'{self.name} ({self.entity_type.name})'
