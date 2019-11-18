from translation.base import Translator
from nltk.tokenize import sent_tokenize, word_tokenize
import os
import requests
import uuid
import json
import html


class MyMemoryTranslator(Translator):
    def __init__(self):
        token = os.environ.get('MYMEMORY_TOKEN')
        if token is None:
            raise Exception(
                'Environment variable "MYMEMORY_TOKEN" must be set')
        self.__mymemory_token = token

    def __request_api(url):
        request = requests.get(url)
        response = request.json()
        formated_response = html.unescape(
            response['responseData']['translatedText'] + ' ')
        return formated_response

    def translate(self, src_text, src_lang, dest_lang):
        endpoint = 'https://api.mymemory.translated.net'
        path = '/get?'
        params = '&langpair=' + src_lang + '|' + dest_lang
        key = '&de=' + self.__mymemory_token
        api_max_chars_per_request = 500

        response = ''

        if len(src_text) > api_max_chars_per_request:
            sentences = sent_tokenize(src_text)
            for sentence in sentences:
                if len(sentence) > api_max_chars_per_request:
                    words = word_tokenize(sentence)
                    for word in words:
                        text = 'q=' + word
                        constructed_url = endpoint + path + text + params + key
                        response += MyMemoryTranslator.__request_api(
                            constructed_url)
                else:
                    text = 'q=' + sentence
                    constructed_url = endpoint + path + text + params + key
                    response += MyMemoryTranslator.__request_api(
                        constructed_url)
            return response
        else:
            text = 'q=' + src_text
            constructed_url = endpoint + path + text + params + key
            response = MyMemoryTranslator.__request_api(constructed_url)
            return response
