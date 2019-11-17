from translation.base import Translator
from googletrans import Translator


class GoogletransTranslator(Translator):
    def __init__(self):
        self.translator = Translator()

    def translate(self, src_text, src_lang, dest_lang):
        return self.translator.translate(src_text, dest=dest_lang, src=src_lang).text
