# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:47:11 2020

@author: 张
"""
#Twitter API#
import tweepy
from tweepy import OAuthHandler
import pandas as pd

consumer_key = '05QRcauWKUjmG6NdoTaJ5RJlR'
consumer_secret = 'cl0cveUs3uKwoDk6jzqMP3NQDlyZqBqjF7LPVDybJehAcyZzjC'
access_token = '1225411734606884865-MQFToe2bFpBTo2WQMe1JM45h9ewqOq'
access_secret = 'xgO4gi1h4HY0g20JDGbnGjomZk1ztv11tI0fzzfRU5Ciq'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,
                  wait_on_rate_limit_notify=True)
maxTweets = 150
tweetsPerQry = 100

emotions = ['#excitement', '#happy', '#pleasant', '#surprise', '#fear', '#angry']
    
for emotion in emotions:
    list1=[]
    number = 0
    sinceId = None
    max_id = -1
    print('class '+ emotion+ ' Downloading max {0} tweets'.format(maxTweets))
    while number < maxTweets:
        if (max_id <= 0):
            if (not sinceId):
                new_tweets = api.search(q=emotion, count=tweetsPerQry, lang='en')
            else:
                new_tweets = api.search(q=emotion, count=tweetsPerQry, since_id=sinceId, lang='en')
        else:
            if (not sinceId):
                new_tweets = api.search(q=emotion, count=tweetsPerQry, max_id=str(max_id - 1), lang='en')
            else:
                new_tweets = api.search(q=emotion, count=tweetsPerQry, max_id=str(max_id - 1), since_id=sinceId, lang='en')
        if not new_tweets:
            print("No more tweets found")
            break
        
        for tweet in new_tweets:
            if number >= 150:
                break
            if (((emotions[0] in tweet.text) and (emotions[0]!= emotion)) or 
                ((emotions[1] in tweet.text) and (emotions[1]!= emotion)) or
                ((emotions[2] in tweet.text) and (emotions[2]!= emotion)) or
                ((emotions[3] in tweet.text) and (emotions[3]!= emotion)) or
                ((emotions[4] in tweet.text) and (emotions[4]!= emotion)) or
                ((emotions[5] in tweet.text) and (emotions[5]!= emotion))):
                continue
            else:
                number+=1
                text = {}
                text['id']= tweet.user
                text['tweet']= tweet.text
                text['created_atinformation']= tweet.created_at
                list1.append(text)
        p = pd.DataFrame(list1)
        p.to_csv(emotion +' '+'q1'+'.csv')
                
                

        print("Downloaded {0} tweets".format(number))
        max_id = new_tweets[-1].id



