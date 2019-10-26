from googletrans import Translator
from nltk.tokenize import sent_tokenize, word_tokenize
import codecs

# Initialization
translator = Translator()
sentences_per_lines = []
translated_sentences_per_lines = []

# Read the text file
text_file = open("input_en.txt", "r")
text_lines = text_file.readlines()

for sentences in text_lines:
    sentences_per_lines.append(sent_tokenize(sentences))

# Translation
source_lang = 'en'
dest_lang = 'fr'

for lines in sentences_per_lines:
    translated_lines = []
    for sentences in lines:
        translated_lines.append(translator.translate(sentences, dest=dest_lang, src=source_lang).text)
    translated_sentences_per_lines.append(translated_lines)

# Output
translated_file = codecs.open("output_fr.txt", "w", "utf-8") 

for lines in translated_sentences_per_lines:
    for sentences in lines:
        translated_file.write(sentences + " ")
    translated_file.write("\n")