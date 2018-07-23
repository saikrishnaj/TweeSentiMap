# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 00:33:43 2018

@author: HP
"""
from __future__ import unicode_literals
c_key='####'
c_secret='$$$$$'
a_key='%%%%%'
a_secret='&&&&&&'
import twitter
api = twitter.Api(consumer_key='####',
                  consumer_secret='$$$$$',
                  access_token_key='%%%%',
                  access_token_secret='&&&&&')

#users = api.GetFriends()

#print([u.screen_name for u in users])
import pandas as pd
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
tweet_list = []
acc_loc_list = []
time_list=[]
date_list=[]
tweet_loc_list=[]
hashtags_list=[]
class listener(StreamListener):
    
    def on_data(self, data):
        """
        #json file method
        dict1=json.loads(data)
        tweet=dict1["text"]
        time_date=dict1["cerated_at"]
        #hashtags=dict1["extended_tweet"]["entities"]["hashtags"]
        time_date=dict1["created_at"]
        if (data.split(',"geo_enabled":')[1].split('lang')[0]) == 'true,"':
            tweet_loc=dict1["place"]["bounding_box"]["coordinates"]
        else:
            tweet_loc='NaN'
        """
        #print(f'{type(dict)}')
        #print(f'this is dict data:\n {dict}\n\n')
        #print(data)
        #print(tweet)
        #filtering the location active accounts
        x = data.split(',"location":')[1].split('url')[0]
        y=x.split('"')
        if(y[1]!=""):
            acc_location=y[1]
            acc_loc_list.append(acc_location)
            tweet = data.split('"text":"')[1].split('source')[0]
            tweet_list.append(tweet)   
            td=data.split('{"created_at":')[1].split('id')[0]
            d=td.split(' ')
            t=d[5].split('"')
            date=d[1]+'-'+d[2]+'-'+t[0]
            time=d[3]
            time_list.append(time)
            date_list.append(date)
            #tweet_list.append(tweet) 
            x={'tweet':tweet_list,'time':time_list,'date':date_list,'acc location':acc_loc_list}
            df = pd.DataFrame(x)
            df.to_csv('C:/Users/HP/OneDrive/Python_Tut/FIFA_sentimap/df_dict_PabloCasado.csv')
        
        """
        #tweet location
        if (data.split(',"geo_enabled":')[1].split('lang')[0]) == 'true,"':
            #tweet_loc=True
            tweet_loc= 'Hi'+(data.split(',"place":')[1].split('contributors')[0])
        else:
            #tweet_loc= False
            tweet_loc = 'Bye'+(data.split(',"place":')[1].split('contributors')[0])
        #tweet_loc = (data.split(',"geo_enabled":')[1].split('lang')[0])
         tweet_loc_list.append(tweet_loc)
        """
        """
        #saving raw data into csv file
        saveFile = open('data_raw.json','a')
        saveFile.write(data)
        #saveFile.write('\t')
        #saveFile.write(location)
        saveFile.write('\n')
        saveFile.close()
        """
        """
        #dataframe method
        time_date_list.append(time_date)
        tweet_list.append(tweet)
        #hashtags_list.append(hashtags)
        """
        return(True)
    
    def on_error(self, status):
        print(status)
#if _name__=="__main__":
auth=OAuthHandler(c_key,c_secret)
auth.set_access_token(a_key,a_secret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track=["Pablo Casado"])
#print(listener.df)
