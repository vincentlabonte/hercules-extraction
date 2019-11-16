from extraction.google import GoogleEntityExtractor
from extraction.dandelion import DandelionEntityExtractor
# from extraction.spacy import SpacyEntityExtractor

if __name__ == "__main__":
    # ee = GoogleEntityExtractor()
    ee = DandelionEntityExtractor()
    entities = ee.extract_entities('Michelangelo Caravaggio, Italian painter, is known for "The Calling of Saint Matthew".')
    for entity in entities:
        print(entity)

    # import spacy
    # nlp = spacy.load('fr_core_news_md')
    # doc = nlp('Michelangelo Caravaggio, Italian painter, is known for "The Calling of Saint Matthew".')
    # print(doc.text)
    # for ent in doc.ents:
    #     print(ent.text, ent.start_char, ent.end_char, ent.label)
    # # for token in doc:
    # #     print(token.text, token.pos_, token.dep_)