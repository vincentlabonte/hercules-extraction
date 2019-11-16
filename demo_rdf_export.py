from coreference.stanford import StanfordCoreferenceResolver
from extraction.dandelion import DandelionEntityExtractor
from export.cidoc_crm import RDFExport
from extraction.base import EntityType

if __name__ == "__main__":
    text = 'Michelangelo Caravaggio, Italian painter, is known for "The Calling of Saint Matthew". Georges Laraque likes him! George\'s wife despises him.'
    # text = 'Georges Laraque likes Michelangelo Caravaggio! George\'s wife despises him.'

    ee = DandelionEntityExtractor()
    entities = ee.extract_entities(text)

    print('Entities:')
    for entity in entities:
        print(entity)
    print()

    cr = StanfordCoreferenceResolver(start_server=False)
    entity_sets = cr.resolve_coreferences(text, entities)

    print('Entities to export: ')
    entities_to_export = []
    for entity_set in entity_sets:
        for entity in entity_set:
            if not entity.entity_type == EntityType.THING:
                entities_to_export.append(entity)
                print(entity.name + ' (' + entity.entity_type.name + ')')
    print()

    exporter = RDFExport()
    exporter.export(entities_to_export, 'http://culture.gouv.qc.ca/entity/', 'http://erlangen-crm.org/170309/', 'turtle')
