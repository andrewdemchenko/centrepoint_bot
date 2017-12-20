# -*- coding: utf-8 -*-
import json
import apiai

from langdetect import detect
from googletrans import Translator


def answer(text):
    language = detect(text)

    if language == 'ar':
        text = translator.translate(text, dest='en', src='ar').text
    else:
        text = text

    request = ai.text_request()
    request.lang, request.query = 'en', text

    result = json.loads(request.getresponse().read()).get('result').get('fulfillment').get('messages')[0].get('speech')

    if language == 'ar':
        result = translator.translate(result, dest='ar', src='en').text
    else:
        result = result

    return result


translator = Translator()
ai = apiai.ApiAI('ab9b502a79c345f9b51f1a83dbdcc053')

# answer = answer(u'مرحبا')