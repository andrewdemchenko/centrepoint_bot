# -*- coding: utf-8 -*-
import json
import apiai


def answer(text):
    request = ai.text_request()
    request.lang, request.query = 'en', text

    result = json.loads(request.getresponse().read()).get('result').get('fulfillment').get('messages')[0].get('speech')

    return result


ai = apiai.ApiAI('ab9b502a79c345f9b51f1a83dbdcc053')
