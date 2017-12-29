import os
import json
import tornado.web
import tornado.ioloop

from langdetect import detect
from get_answer import answer
from location import find_near
from googletrans import Translator
from send_email import email as send
from location import validate_location
from validate_email import validate_email


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        data = self.get_argument('data')
        data = json.loads(data)

        message = data.get('url')

        try:
            language = detect(message)
        except Exception:
            language = 'en'

        print language

        if language == 'ar':
            message = translator.translate(message, dest='en', src='ar').text
        else:
            pass

        print message

        email = validate_email(message, verify=True)
        location = validate_location(message)

        if email == True:
            send(message)
            result = 'Thank you. Our support will contact to you soon.'
        elif location != None and message.title() not in hello and len(message) > 5:
            data = find_near(location)
            result = 'The nearest Centrepoint is in {} only at {} kilometers from you'.format(data[2], round(data[6], 2))
        else:
            try:
                result = answer(message)
            except Exception:
                result = 'Ooops. Something goes wrong. Please, try again.'

        if language == 'ar':
            result = translator.translate(result, dest='ar', src='en').text
        else:
            result = result

        self.write(json.dumps({'result': [result]}))

translator = Translator()

hello = ['Hello', 'Good Day', 'Hi', 'Greetings']

settings = {'static_path': os.path.join(os.path.dirname(__file__), "static"),
            'debug': True, }

application = tornado.web.Application([
    (r"/", MainHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.current().start()
