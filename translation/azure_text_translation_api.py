import os, requests, uuid, json

class AzureTextTranslationAPI():
    def translate(src_text, src_lang, dest_lang): 
        key_var_name = 'TRANSLATOR_TEXT_SUBSCRIPTION_KEY'
        if not key_var_name in os.environ:
            raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
        subscription_key = os.environ[key_var_name]

        # If you encounter any issues with the base_url or path, make sure
        # that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
        endpoint = "https://api-nam.cognitive.microsofttranslator.com/"
        path = '/translate?api-version=3.0'
        params = '&from=' + src_lang + '&to=' + dest_lang
        constructed_url = endpoint + path + params

        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text' : src_text
        }]
        request = requests.post(constructed_url, headers=headers, json=body)
        response = request.json()

        return response[0]['translations'][0]['text']