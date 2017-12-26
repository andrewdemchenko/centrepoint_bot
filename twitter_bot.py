# # coding: utf-8
# import tweepy
#
# from time import localtime, strftime
#
# replied = []
# message = 'Hello'
#
# consumer_key = 'He8lWDsfmkVkvAKITiJEcPPbW'
# consumer_secret = 'tvi3vXBLUyiZJwiQ5xqHEgBgmRkOC8sLwMo8xtz34ezc2Sauos'
#
# access_key = "1701503700-74EvUVMboYMw8WvAXbRL7nuUGlqGYtjI8TyDqaE"
# access_secret = "LQyLLAzEpGVQ2azorgYyVy7wNOrrmnoP98vefmzpRmiQS"
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_key, access_secret)
#
# api = tweepy.API(auth)
# request = api.search('qwerty678606')
#
#
# for i in request:
#     if i.id not in replied:
#         api.update_status('@' + i.user.screen_name + ' ' + message, i.id)
#         replied.append(i.id)
#
#         print strftime('[%d/%m %H:%M:%S]', localtime()) + ' Reply to @' + str(i.user.screen_name) + ': ' + message




# !/usr/bin/env python
import tweepy, sys, time
from random import randint

CONSUMER_KEY = 'He8lWDsfmkVkvAKITiJEcPPbW'
CONSUMER_SECRET = 'tvi3vXBLUyiZJwiQ5xqHEgBgmRkOC8sLwMo8xtz34ezc2Sauos'
ACCESS_TOKEN = "1701503700-74EvUVMboYMw8WvAXbRL7nuUGlqGYtjI8TyDqaE"
ACCESS_TOKEN_SECRET = "LQyLLAzEpGVQ2azorgYyVy7wNOrrmnoP98vefmzpRmiQS"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

i = '@mecsikanamama'

i = i.rstrip()
s = api.direct_messages()