from extraction.base import EntityExtractor, Entity, EntityType
from google.cloud import language

class GoogleEntityExtractor(EntityExtractor):

    # https://cloud.google.com/natural-language/docs/reference/rest/v1/Entity#Type
    __google_type_to_entity_type = {
        PERSON: EntityType.PERSON,
        LOCATION: EntityType.PLACE,
        ORGANIZATION: EntityType.GROUP,
        EVENT: EntityType.EVENT,
        WORK_OF_ART: EntityType.MANMADEOBJECT,
        ADDRESS: EntityType.ADDRESS,
        DATE: EntityType.DATE
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
            encoding_type='UTF32'
        )
        # print(response)
        return self.__convert_entities(response.entities)

    def __convert_entities(self, entities):
        converted_entities = []
        for entity in entities:
            entity_type = EntityType(entity.type)
            converted_entity = Entity(entity.name, entity_type)
            converted_entities.append(converted_entity)
        return converted_entities

    def __convert_types(self, types):
        entity_type = EntityType.THING
        if len(types) > 0:
            for t in types:
                if t in GoogleEntityExtractor.__google_type_to_entity_type:
                    entity_type = GoogleEntityExtractor.__google_type_to_entity_type[t]
                    break
        return entity_type
