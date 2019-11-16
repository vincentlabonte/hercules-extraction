from coreference.stanford import StanfordCoreferenceResolver
from extraction.dandelion import DandelionEntityExtractor

if __name__ == "__main__":
    text = 'Michelangelo Caravaggio, Italian painter, is known for "The Calling of Saint Matthew". Georges Laraque likes him! George\'s wife despises him.'
    # text = 'Georges Laraque likes Michelangelo Caravaggio! George\'s wife despises him.'

    ee = DandelionEntityExtractor()
    entities = ee.extract_entities(text)

    print('Entities before coreference resolution')
    for entity in entities:
        print(entity)
    print()

    cr = StanfordCoreferenceResolver(start_server=False)
    entity_sets = cr.resolve_coreferences(text, entities)

    print('Entities after coreference resolution')
    for entity_set in entity_sets:

        print('{ ' + ', '.join([str(entity) for entity in entity_set]) + ' }')
    print()
    # print(coreferences)
    # for coreference in coreferences:
    #     for item in coreference:
    #         print(text[item[0]:item[1]], end='  ---  ')
    #     print()
    # for coreference in coreferences:
    #     print(coreference)