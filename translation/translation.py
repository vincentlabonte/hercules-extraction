from googletrans import Translator
from nltk.tokenize import sent_tokenize, word_tokenize
import codecs
import sys

def read_file(src_text):
    sentences_per_lines = []
    text_file = open(src_text, "r")
    text_lines = text_file.readlines()

    for sentences in text_lines:
        sentences_per_lines.append(sent_tokenize(sentences))
    return sentences_per_lines

def translate_sentences_per_lines(sentences_per_lines, src_lang, dest_lang):
    translated_sentences_per_lines = []
    for lines in sentences_per_lines:
        translated_lines = []
        for sentences in lines:
            translated_lines.append(translator.translate(sentences, dest=dest_lang, src=src_lang).text)
        translated_sentences_per_lines.append(translated_lines)
    return translated_sentences_per_lines

def export_translated_file(translated_sentences_per_lines, dest_text):
    translated_file = codecs.open(dest_text, "w", "utf-8") 

    for lines in translated_sentences_per_lines:
        for sentences in lines:
            translated_file.write(sentences + " ")
        translated_file.write("\n")

def translate(src_text, src_lang, dest_text, dest_lang):
    sentences_per_lines = read_file(src_text)
    translated_sentences_per_lines = translate_sentences_per_lines(sentences_per_lines, src_lang, dest_lang)
    return export_translated_file(translated_sentences_per_lines, dest_text)

if __name__ == "__main__":
    src_text = sys.argv[1]
    src_lang = sys.argv[2]
    dest_text = sys.argv[3]
    dest_lang = sys.argv[4]

    # Initialization
    translator = Translator()

    #Translation
    translate(src_text, src_lang, dest_text, dest_lang)