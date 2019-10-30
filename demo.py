from translation.googletrans import Googletrans
from translation.google_cloud_api import GoogleCloudAPI
from extraction.google import GoogleEntityExtractor
from extraction.dandelion import DandelionEntityExtractor

if __name__ == "__main__":
    text = 'La première église Notre-Dame fut construite à partir de 1672 sur un emplacement déterminé par Dollier de Casson, ' \
                'dans l\'axe de la rue Notre-Dame sur l\'actuelle Place d\'Armes. Peu à peu l\'église ne suffit plus à répondre aux ' \
                'besoins de la population. La fabrique de la paroisse envisagea donc, au début du XIXe siècle la construction d\'une ' \
                'nouvelle église. Le projet de construction fut confié à l\'architecte new-yorkais d\'origine irlandaise James O\'Donnell ' \
                'à qui on demanda de réaliser la plus vaste et la plus belle église catholique d\'Amérique du Nord. O\'Donnell arriva à ' \
                'Montréal en octobre 1823 et proposa un projet aux marguilliers qui l\'acceptèrent rapidement.'

    print('Original text:')
    print(text)

    print()

    google_entity_extractor = GoogleEntityExtractor()
    print('Entity extracted with Google from the original text:')
    entities = google_entity_extractor.extract_entity(text)
    for entity in entities:
        print(entity)

    print()
    
    dandelion_entity_extractor = DandelionEntityExtractor()
    print('Entity extracted with Dandelion from the original text:')
    entities = dandelion_entity_extractor.extract_entity(text)
    for entity in entities:
        print(entity)

    print()

    print('Translated text (googletrans):')
    translated_text_googletrans = Googletrans.translate(text, 'auto', 'en')
    print(translated_text_googletrans)

    print()

    print('Entity extracted with Google from the translated text (googletrans):')
    entities = google_entity_extractor.extract_entity(translated_text_googletrans)
    for entity in entities:
        print(entity)

    print()

    print('Entity extracted with Dandelion from the translated text (googletrans):')
    entities = dandelion_entity_extractor.extract_entity(translated_text_googletrans)
    for entity in entities:
        print(entity)

    print()

    print('Translated text (Google Cloud API):')
    translated_text_google_cloud_api = GoogleCloudAPI.translate(text, 'fr', 'en')
    print(translated_text_google_cloud_api)

    print()

    print('Entity extracted with Google from the translated text (Google Cloud API):')
    entities = google_entity_extractor.extract_entity(translated_text_google_cloud_api)
    for entity in entities:
        print(entity)

    print()

    print('Entity extracted with Dandelion from the translated text (Google Cloud API):')
    entities = dandelion_entity_extractor.extract_entity(translated_text_google_cloud_api)
    for entity in entities:
        print(entity)
