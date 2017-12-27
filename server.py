import os
import json
import tornado.web
import tornado.ioloop

from get_answer import answer
from location import find_near
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
        email = validate_email(message, verify=True)
        location = validate_location(message)

        if email == True:
            send(message)
            result = 'Thank you. Our support will contact to you soon.'
        elif location != None:
            result = 'This is location'
            find_near(location)
        else:
            try:
                result = answer(message)
            except Exception:
                result = 'Ooops. Something goes wrong. Please, try again.'

        self.write(json.dumps({'result': [result]}))


settings = {'static_path': os.path.join(os.path.dirname(__file__), "static"),
            'debug': True, }

application = tornado.web.Application([
    (r"/", MainHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.current().start()
