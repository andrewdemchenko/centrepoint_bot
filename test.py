from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

import json

CONSUMER_KEY = 'ChZZ5nDwuyteOF0muX1wlEY9T'
CONSUMER_SECRET = 'pRetooDE7La5AlDVaGuBYCIN2kzbBi0Cv4i9oEx57hWVy5LERq'

ACCESS_TOKEN = '1701503700-KptPGwrh9dGxgWZDiRjVz9Ok6GDkZ9d0KBd20ip'
ACCESS_TOKEN_SECRET = '8CcOHvQEPOgH58fNmFnl99GjGMbkcl2gEjxxZNNdaATfG'


class EventListener(StreamListener):
    def on_data(self, data):
        data = (json.loads(data))

        try:
            sender = data.get('direct_message').get('sender').get('screen_name')
            question = data.get('direct_message').get('text')

            try:
                api.send_direct_message(user=sender, text=question)

                print('Sender: ', sender)
                print('Question: ', question)
                print('Answer: ', question)
            except Exception:
                print('*--- Rate limit ---*', '\n')

        except Exception:
            print ('*--- Another user activity on the page ---*', '\n')

        return True

    def on_error(self, status):
        print(status)


listener = EventListener()

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = API(auth)

stream = Stream(auth, listener)
stream.userstream()