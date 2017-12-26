import os
import json
import tornado.web
import tornado.ioloop

from send_email import email as lol
from get_answer import answer
from validate_email import validate_email


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        data = self.get_argument('data')
        data = json.loads(data)

        message = data.get('url')
        email = validate_email(message, verify=True)
        print email

        if email == True:
            lol(message)
            result = 'Thank you. Our support will contact to you soon.'
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
