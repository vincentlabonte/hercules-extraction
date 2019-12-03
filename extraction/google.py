from extraction.base import EntityExtractor, Entity, EntityType
from google.cloud import language
from unicodedata import normalize


class GoogleEntityExtractor(EntityExtractor):

    # https://cloud.google.com/natural-language/docs/reference/rest/v1/Entity#Type
    __google_type_to_entity_type = {
        'UNKNOWN': EntityType.THING,
        'PERSON': EntityType.PERSON,
        'LOCATION': EntityType.PLACE,
        'ORGANIZATION': EntityType.GROUP,
        'EVENT': EntityType.EVENT,
        'WORK_OF_ART': EntityType.MANMADEOBJECT,
        'CONSUMER_GOOD': EntityType.THING,
        'OTHER': EntityType.THING,
        'PHONE_NUMBER': EntityType.THING,
        'ADDRESS': EntityType.ADDRESS,
        'DATE': EntityType.DATE,
        'NUMBER': EntityType.THING,
        'PRICE': EntityType.THING
    }

    def __init__(self):
        self.__client = language.LanguageServiceClient()

    def extract_entities(self, text):
        document = language.types.Document(
            content=text,
            type=language.enums.Document.Type.PLAIN_TEXT
        )
        response = self.__client.analyze_entities(
            document=document,
            encoding_type=language.enums.EncodingType.UTF32
        )
        return self.__convert_entities(response.entities)

    def __convert_entities(self, entities):
        converted_entities = []
        for entity in entities:
            entity_type_name = language.enums.Entity.Type(entity.type).name
            entity_type = GoogleEntityExtractor.__google_type_to_entity_type[entity_type_name]
            converted_entity = Entity(entity.name, entity_type, None, None)
            converted_entities.append(converted_entity)
        return converted_entities
