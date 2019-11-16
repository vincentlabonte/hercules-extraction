from translation.base import Translator
from google.cloud import translate_v2 as translate
import html


class GoogleCloudTranslator(Translator):
    def __init__(self):
        self.translate_client = translate.Client()

    def translate(self, src_text, src_lang, dest_lang):
        return html.unescape(self.translate_client.translate(src_text, source_language=src_lang, target_language=dest_lang)['translatedText'])
