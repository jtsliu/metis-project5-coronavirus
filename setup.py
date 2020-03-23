import pandas as pd

import os
import linecache
from datetime import datetime

import tweepy
from credentials import *

# Create credentials.py in working directory with 
# your application's key and secret. API_KEY and API_SECRET
auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)
    
state_list = ['california', 'colorado', 'florida', 
              'georgia', 'idaho', 'illinois', 
              'louisiana', 'massachusetts', 'newyork',
              'tennessee', 'texas', 'washington']