from translation.base import Translation
from googletrans import Translator

class Googletrans(Translation):
    def translate(self, src_text, src_lang, dest_lang):
        translator = Translator()
        return translator.translate(src_text, dest=dest_lang, src=src_lang).text