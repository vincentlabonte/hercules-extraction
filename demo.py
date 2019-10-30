from extraction.google import GoogleEntityExtractor
from extraction.dandelion import DandelionEntityExtractor

from translation.googletrans import Googletrans
from translation.google_cloud import GoogleCloud
from translation.azure_text import AzureText
from translation.my_memory import MyMemory

if __name__ == "__main__":
    text = 'La première église Notre-Dame fut construite à partir de 1672 sur un emplacement déterminé par Dollier de Casson, ' \
                'dans l\'axe de la rue Notre-Dame sur l\'actuelle Place d\'Armes. Peu à peu l\'église ne suffit plus à répondre aux ' \
                'besoins de la population. La fabrique de la paroisse envisagea donc, au début du XIXe siècle la construction d\'une ' \
                'nouvelle église. Le projet de construction fut confié à l\'architecte new-yorkais d\'origine irlandaise James O\'Donnell ' \
                'à qui on demanda de réaliser la plus vaste et la plus belle église catholique d\'Amérique du Nord. O\'Donnell arriva à ' \
                'Montréal en octobre 1823 et proposa un projet aux marguilliers qui l\'acceptèrent rapidement.'

    # ----------- Translation ------------ #
    translated_text_googletrans = Googletrans.translate(Googletrans, text, 'fr', 'en')
    translated_text_google_cloud = GoogleCloud.translate(GoogleCloud, text, 'fr', 'en')
    translated_text_azure = AzureText.translate(AzureText, text, 'fr', 'en')
    translated_text_mymemory = MyMemory.translate(MyMemory, text, 'fr', 'en')

    texts = [
        (None, text),
        ("googletrans", translated_text_googletrans),
        ("Google Cloud", translated_text_google_cloud),
        ("Azure Text", translated_text_azure),
        ("MyMemory", translated_text_mymemory),
    ]

    # ----------- Extraction ------------ #
    google_entity_extractor = GoogleEntityExtractor()
    dandelion_entity_extractor = DandelionEntityExtractor()

    extractors = [
        ("Google", google_entity_extractor),
        ("Dandelion", dandelion_entity_extractor),
    ]

    # ----------- Output ------------ #
    for translator_name, text in texts:
        text_name ='Original text:' if translator_name is None else (
            f'Translated text ({translator_name})')
        print(f'{text_name}:')
        print(text, end='\n\n')
        for extractor_name, extractor in extractors:
            print(f'Entity extracted with {extractor_name} from the {text_name}:')
            entities = extractor.extract_entity(text)
            for entity in entities:
                print(entity)
            print()
    