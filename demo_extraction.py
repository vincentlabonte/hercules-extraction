from extraction.google import GoogleEntityExtractor

if __name__ == "__main__":
    ee = GoogleEntityExtractor()
    entities = ee.extract_entity('Michelangelo Caravaggio, Italian painter, is known for "The Calling of Saint Matthew".')
    for entity in entities:
        print(entity)