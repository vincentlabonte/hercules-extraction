from translation.googletrans import Googletrans
from translation.google_cloud import GoogleCloud
from translation.azure_text import AzureText
from translation.my_memory import MyMemory

from extraction.google import GoogleEntityExtractor

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/frank/Google/Hercules-f7fc5c09aeb5.json"
os.environ["TRANSLATOR_TEXT_SUBSCRIPTION_KEY"]="18dbb72b6fa24cf29bd29fa7c03a60a2"

if __name__ == "__main__":
    text = 'La première église Notre-Dame fut construite à partir de 1672 sur un emplacement déterminé par Dollier de Casson, ' \
                'dans l\'axe de la rue Notre-Dame sur l\'actuelle Place d\'Armes. Peu à peu l\'église ne suffit plus à répondre aux ' \
                'besoins de la population. La fabrique de la paroisse envisagea donc, au début du XIXe siècle la construction d\'une ' \
                'nouvelle église. Le projet de construction fut confié à l\'architecte new-yorkais d\'origine irlandaise James O\'Donnell ' \
                'à qui on demanda de réaliser la plus vaste et la plus belle église catholique d\'Amérique du Nord. O\'Donnell arriva à ' \
                'Montréal en octobre 1823 et proposa un projet aux marguilliers qui l\'acceptèrent rapidement.'

    # ----------- Original text ------------ #
    print('Original text:')
    print(text)

    print()

    extractor = GoogleEntityExtractor()
    print('Entity extracted from the original text:')
    entities = extractor.extract_entity(text)
    for entity in entities:
        print(entity)
    # -------------------------------------- #

    print()

    # ------------ googletrans ------------- #
    print('Translated text (googletrans):')
    translated_text_googletrans = Googletrans.translate(text, 'fr', 'en')
    print(translated_text_googletrans)

    print()

    print('Entity extracted from the translated text (googletrans):')
    entities = extractor.extract_entity(translated_text_googletrans)
    for entity in entities:
        print(entity)
    # -------------------------------------- #

    print()

    # ------------ Google Cloud ------------ #
    print('Translated text (Google Cloud):')
    translated_text_google_cloud = GoogleCloud.translate(text, 'fr', 'en')
    print(translated_text_google_cloud)

    print()

    print('Entity extracted from the translated text (Google Cloud):')
    entities = extractor.extract_entity(translated_text_google_cloud)
    for entity in entities:
        print(entity)
    # -------------------------------------- #

    print()

    # ------------- Azure Text ------------- #
    print('Translated text (Azure Text):')
    translated_text_azure = AzureText.translate(text, 'fr', 'en')
    print(translated_text_azure)

    print()

    print('Entity extracted from the translated text (Azure Text):')
    entities = extractor.extract_entity(translated_text_azure)
    for entity in entities:
        print(entity)
    # -------------------------------------- #

    print()

    # -------------- MyMemory -------------- #
    print('Translated text (MyMemory):')
    translated_text_mymemory = MyMemory.translate(text, 'fr', 'en')
    print(translated_text_mymemory)

    print()

    print('Entity extracted from the translated text (MyMemory):')
    entities = extractor.extract_entity(translated_text_mymemory)
    for entity in entities:
        print(entity)
    # -------------------------------------- #
