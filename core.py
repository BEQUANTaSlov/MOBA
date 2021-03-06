from numpy.lib.arraysetops import _in1d_dispatcher
import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys
import pandas as pd
import time
import pandas as pd
import numpy as np
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.wordnet import WordNetLemmatizer 
#import stanfordnlp
#stanfordnlp.download('en')
from aspectAnalysis import aspect_sentiment_analysis
import stanza
stanza.download('en')

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

API = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

nytimeslatesttweetID = 1459588611935023104
WSJlatesttweetID = 1459588611935023104

alpha = 0
while alpha <= 1:

    #NEW YORK TIMES
    #NEW YORK TIMES
    #NEW YORK TIMES
    #NEW YORK TIMES
    #NEW YORK TIMES
    #NEW YORK TIMES

    user = api.get_user(screen_name = "nytimes")
    NYT_ID = user.id_str
    try:
        for tweet in API.user_timeline(user_id = NYT_ID, count=1, since_id = nytimeslatesttweetID, include_rts = False, truncated = False, tweet_mode = "extended"):

            full_text = tweet.full_text
            tweets = []
            count = 1
            print(count)
            count += 1

            import re
            nytTextOnly = re.sub(r' https://t.co/\w{10}', '', tweet.full_text)

            #print(tweet)
            nytimesdata = {
                "Tweet ID": tweet.id_str,
                "timestamp": tweet.created_at,
                "Publication": "The New York Times",
                #"Content": tweet.text,
                "Content": nytTextOnly,
                #"Article Link": tweet.expanded_url,
                "Full Content": full_text,
            }

            print (nytimesdata)

            nytimeslatesttweetID = tweet.id_str


            #   NYT ANALYSIS
            stop_words = set(stopwords.words('english'))
            nlp = stanza.Pipeline('en')
            txt = nytTextOnly

            print(aspect_sentiment_analysis(txt, stop_words, nlp))

        #nytimes()
    except:
        continue

    ##WSJ
    ##WSJ
    ##WSJ
    ##WSJ

    user = api.get_user(screen_name = "wsj")
    WSJ_ID = user.id_str

    try:
        for tweet in API.user_timeline(user_id = WSJ_ID, count=1, since_id = WSJlatesttweetID, include_rts = False, truncated = False, tweet_mode = "extended"):

            tweets = []
            count = 1
            print(count)
            count += 1

            full_text = tweet.full_text
            import re
            wsjTextOnly = re.sub(r' https://t.co/\w{10}', '', tweet.full_text)

            #print(tweet)
            WSJdata = {
                "Tweet ID": tweet.id_str,
                "timestamp": tweet.created_at,
                "Publication": "The Wall Street Journal",
                #"Content": tweet.text,
                "Content": wsjTextOnly,
                #"Article Link": tweet.expanded_url,
                "Full Content": full_text,
            }

            print (WSJdata)

            WSJlatesttweetID = tweet.id_str
    except:
        continue

    alpha = alpha + 1
    print ("Round ")
    print(alpha)
    print("completed")
    time.sleep(600)
    #thus another revolution