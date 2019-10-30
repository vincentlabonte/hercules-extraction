from translation.base import Translation
from nltk.tokenize import sent_tokenize, word_tokenize
import os, requests, uuid, json
import html

class MyMemory(Translation):
    def __request_api(url):
        request = requests.get(url)
        response = request.json()
        formated_response = html.unescape(response['responseData']['translatedText'] + " ")
        return formated_response

    def translate(self, src_text, src_lang, dest_lang):
        key_var_name = 'MYMEMORY_API_KEY'
        if not key_var_name in os.environ:
            raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
        subscription_key = os.environ[key_var_name]

        endpoint = 'https://api.mymemory.translated.net'
        path = '/get?'
        params = '&langpair=' + src_lang + '|' + dest_lang
        key = '&de=' + subscription_key
        api_max_chars_per_request = 500

        response = ""

        if len(src_text) > api_max_chars_per_request:
            sentences = sent_tokenize(src_text)
            for sentence in sentences:
                if len(sentence) > api_max_chars_per_request:
                    words = word_tokenize(sentence)
                    for word in words:
                        text = 'q=' + word
                        constructed_url = endpoint + path + text + params + key
                        response += MyMemory.__request_api(constructed_url)
                else:
                    text = 'q=' + sentence
                    constructed_url = endpoint + path + text + params + key
                    response += MyMemory.__request_api(constructed_url)
            return response
        else:
            text = 'q=' + src_text
            constructed_url = endpoint + path + text + params + key
            response = MyMemory.__request_api(constructed_url)
            return response