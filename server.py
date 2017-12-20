import os
import json
import tornado.web
import tornado.ioloop

from get_answer import answer


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        data = self.get_argument('data')
        data = json.loads(data)

        message = data.get('url')

        result = answer(message)

        self.write(json.dumps({'result': [result]}))


settings = {'static_path': os.path.join(os.path.dirname(__file__), "static"),
            'debug': True,}

application = tornado.web.Application([
    (r"/", MainHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.current().start()