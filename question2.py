# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:10:05 2020

@author: 张
"""

import pandas as pd
import enchant
from enchant.tokenize import get_tokenizer

emotions = ['#excitement', '#happy', '#pleasant', '#surprise', '#fear', '#angry']


def isEmoji(content):
    if not content:
        return False
    if u"\U0001F600" <= content and content <= u"\U0001F64F":
        return True
    elif u"\U0001F300" <= content and content <= u"\U0001F5FF":
        return True
    elif u"\U0001F680" <= content and content <= u"\U0001F6FF":
        return True
    elif u"\U0001F1E0" <= content and content <= u"\U0001F1FF":
        return True
    else:
        return False
#https://blog.csdn.net/i_chenjiahui/article/details/51752189
tknzr = get_tokenizer("en_US")
d = enchant.Dict("en_US")
for emotion in emotions:
    list1=[]
    df = pd.read_csv(emotion +'.csv')
    df= df.drop_duplicates(subset='tweet')
    for t in df['tweet']:
        str1=''
        for w in tknzr(t):
            if isEmoji(w[0]):
                str1=str1 + w[0]+ ' '
            elif w[0].isalpha():
                b=str(w[0])
                b=b.lower()
                if d.check(b):
                    str1=str1 + b+ ' '
                else:
                    a=d.suggest(b)
                    if len(a)>0:
                        str1=str1+a[0]+' '
        text = {}
        text['id']= tweet.user
        text['tweet']= str1
        text['created_atinformation']= tweet.created_at
        list1.append(text)
        print(str1)
    p = pd.DataFrame(list1)
    p.to_csv(emotion +' '+'q2'+'.csv')                












