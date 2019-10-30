from google.cloud import translate_v2 as translate
import html

class GoogleCloud():
    def translate(src_text, src_lang, dest_lang):
        translate_client = translate.Client()
        return html.unescape(translate_client.translate(src_text, source_language=src_lang, target_language=dest_lang)['translatedText'])