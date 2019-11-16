from translation.base import Translator
import os
import requests
import uuid
import json

class AzureTranslator(Translator):
    def __init__(self):
        token = os.environ.get('AZURE_TOKEN')
        if token is None:
            raise Exception('Environment variable "AZURE_TOKEN" must be set')
        self.__azure_token = token

    def translate(self, src_text, src_lang, dest_lang):
        endpoint = 'https://api-nam.cognitive.microsofttranslator.com/'
        path = '/translate?api-version=3.0'
        params = '&from=' + src_lang + '&to=' + dest_lang
        constructed_url = endpoint + path + params

        headers = {
            'Ocp-Apim-Subscription-Key': self.__azure_token,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        body = [{
            'text': src_text
        }]
        request = requests.post(constructed_url, headers=headers, json=body)
        response = request.json()

        return response[0]['translations'][0]['text']
