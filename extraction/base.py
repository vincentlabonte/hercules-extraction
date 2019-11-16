from enum import Enum

class EntityExtractor():
    def extract_entities(self, text):
        pass

class EntityType(Enum):
    EVENT = 0
    ACTIVITY = 1
    PERSON = 2
    MANMADEOBJECT = 3
    ADDRESS = 4
    DATE = 5
    PLACE = 6
    THING = 7
    GROUP = 8

class Entity():
    def __init__(self, name, entity_type, start_offset, end_offset):
        self.name = name
        self.entity_type = entity_type
        self.start_offset = start_offset
        self.end_offset = end_offset
    
    def __str__(self):
        return f'{self.name} ({self.entity_type.name})'
