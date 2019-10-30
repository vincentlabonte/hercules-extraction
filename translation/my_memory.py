import os, requests, uuid, json
from nltk.tokenize import sent_tokenize
import html

class MyMemory():
    def request_api(url):
        request = requests.get(url)
        response = request.json()
        formated_response = html.unescape(response['responseData']['translatedText'] + " ")
        return formated_response

    def translate(src_text, src_lang, dest_lang):
        api_key = 'francis150150@hotmail.com'
        endpoint = 'https://api.mymemory.translated.net'
        path = '/get?'
        params = '&langpair=' + src_lang + '|' + dest_lang
        key = '&de=' + api_key
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
                        response += MyMemory.request_api(constructed_url)
                else:
                    text = 'q=' + sentence
                    constructed_url = endpoint + path + text + params + key
                    response += MyMemory.request_api(constructed_url)
            return response
        else:
            text = 'q=' + src_text
            constructed_url = endpoint + path + text + params + key
            response = MyMemory.request_api(constructed_url)
            return response