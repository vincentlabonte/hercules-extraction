from extraction.base import EntityExtractor, Entity, EntityType
from google.cloud import language

class GoogleEntityExtractor(EntityExtractor):

    def __init__(self):
        self.__client = language.LanguageServiceClient()

    def extract_entity(self, text):
        document = language.types.Document(
            content=text,
            type=language.enums.Document.Type.PLAIN_TEXT
        )
        response = self.__client.analyze_entities(
            document=document,
            encoding_type='UTF32'
        )
        return GoogleEntityExtractor.__convert_entities(response.entities)

    def __convert_entities(entities):
        converted_entities = []
        for entity in entities:
            entity_type = EntityType(entity.type)
            converted_entity = Entity(entity.name, entity_type)
            converted_entities.append(converted_entity)
        return converted_entities
