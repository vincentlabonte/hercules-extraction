from dandelion import DataTXT
from extraction.base import EntityExtractor, Entity, EntityType
import os

class DandelionEntityExtractor(EntityExtractor):

    # http://mappings.dbpedia.org/server/ontology/classes/
    __dbpedia_type_to_entity_type = {
        'http://dbpedia.org/ontology/Person': EntityType.PERSON,
        'http://dbpedia.org/ontology/Place': EntityType.PLACE,
        'http://dbpedia.org/ontology/Organisation': EntityType.GROUP,
        'http://dbpedia.org/ontology/Group': EntityType.GROUP,
        'http://dbpedia.org/ontology/Event': EntityType.EVENT,
        'http://dbpedia.org/ontology/TimePeriod': EntityType.DATE,
        'http://dbpedia.org/ontology/Activity': EntityType.ACTIVITY,
        'http://dbpedia.org/ontology/Work': EntityType.MANMADEOBJECT
    }

    def __init__(self):
        token = os.environ.get('DANDELION_TOKEN')
        if token is None:
            raise Exception('Environment variable "DANDELION_TOKEN" must be set')
        self.__datatxt = DataTXT(token=token)

    def extract_entities(self, text):
        response = self.__datatxt.nex(text, include_types=True)
        return self.__convert_entities(response.annotations)

    def __convert_entities(self, annotations):
        converted_entities = []
        for annotation in annotations:
            entity_type = self.__convert_types(annotation.types)
            converted_entity = Entity(annotation.label, entity_type, annotation.start, annotation.end)
            converted_entities.append(converted_entity)
        return converted_entities

    def __convert_types(self, types):
        entity_type = EntityType.THING
        if len(types) > 0:
            for t in types:
                if t in DandelionEntityExtractor.__dbpedia_type_to_entity_type:
                    entity_type = DandelionEntityExtractor.__dbpedia_type_to_entity_type[t]
                    break
        return entity_type