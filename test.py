# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import error
from tweepy import API

import json
import apiai
import smtplib
import pandas as pd

from langdetect import detect
from googletrans import Translator
from geopy.distance import vincenty
from geopy.geocoders import Nominatim
from validate_email import validate_email

CONSUMER_KEY = 'ChZZ5nDwuyteOF0muX1wlEY9T'
CONSUMER_SECRET = 'pRetooDE7La5AlDVaGuBYCIN2kzbBi0Cv4i9oEx57hWVy5LERq'

ACCESS_TOKEN = '1701503700-KptPGwrh9dGxgWZDiRjVz9Ok6GDkZ9d0KBd20ip'
ACCESS_TOKEN_SECRET = '8CcOHvQEPOgH58fNmFnl99GjGMbkcl2gEjxxZNNdaATfG'


def send_email(email):
    bot = 'centrepointbot@gmail.com'
    user = email
    support = 'nordstone333@gmail.com'

    password = 'qwerty678606'

    msg = '\r\n'.join([
        'From: {}'.format(bot),
        'To: {}'.format(support),
        'Subject: Centrepoint Bot Report',
        '',
        'Hi! {} have some questions. Write to him, please.'.format(user)
    ])

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.login(bot, password)
    server.sendmail(bot, [support], msg)
    server.quit()


def validate_location(location):
    return geolocator.geocode(location)


def find_near(location):
    lat, long = location.latitude, location.longitude

    temp = ['Country', 'City', 'Street', 'Lat', 'Long', 'Time', 1000000]

    for i in data:
        distance = vincenty((lat, long), (i[3], i[4])).kilometers
        i.append(distance)

        if float(temp[6]) > distance:
            temp = i
        else:
            pass

    return temp


def answer(text):
    request = ai.text_request()
    request.lang, request.query = 'en', text

    result = json.loads(request.getresponse().read()).get('result').get('fulfillment').get('messages')[0].get('speech')

    return result


def get_answer(message):
    try:
        language = detect(message)
    except Exception:
        language = 'en'

    if language == 'ar':
        message = translator.translate(message, dest='en', src='ar').text

    email = validate_email(message, verify=True)
    location = validate_location(message)

    if email == True:
        send_email(message)
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

    return result


class EventListener(StreamListener):
    def on_data(self, data):
        data = (json.loads(data))

        try:
            sender = data.get('direct_message').get('sender').get('screen_name')
            question = data.get('direct_message').get('text')

            if sender != 'stark_man_usa':
                try:
                    api.send_direct_message(user=sender, text=get_answer(question))

                    print('Sender: ', sender)
                    print('Question: ', question, '\n')
                except error.RateLimitError:
                    print('*--- Rate limit ---*', '\n')

        except Exception:
            print ('*--- Another user activity on the page ---*', '\n')

        return True

    def on_error(self, status):
        print(status)


geolocator = Nominatim()
translator = Translator()
hello = ['Hello', 'Good Day', 'Hi', 'Greetings']
ai = apiai.ApiAI('ab9b502a79c345f9b51f1a83dbdcc053')
data = pd.read_excel('./data/location.xlsx').as_matrix().tolist()


listener = EventListener()

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

stream = Stream(auth, listener)
stream.userstream()