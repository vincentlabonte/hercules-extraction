from extraction.google import GoogleEntityExtractor
from extraction.dandelion import DandelionEntityExtractor

if __name__ == "__main__":
    # ee = GoogleEntityExtractor()
    ee = DandelionEntityExtractor()
    entities = ee.extract_entity('Michelangelo Caravaggio, Italian painter, is known for "The Calling of Saint Matthew".')
    for entity in entities:
        print(entity)
    