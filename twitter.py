import os
import json
import requests
import base64

credentials = {}
credentials['CONSUMER_KEY'] = os.environ['TWITTER_API_KEY']
credentials['CONSUMER_SECRET'] = os.environ['TWITTER_API_KEY_SECRET']
credentials['ACCESS_TOKEN'] = os.environ['TWITTER_ACCESS_TOKEN']
credentials['ACCESS_SECRET'] = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
base_url = 'https://api.twitter.com/'

def createAccessToken():
    #Define your keys from the developer portal
    client_key = credentials['CONSUMER_KEY']
    client_secret = credentials['CONSUMER_SECRET']
    #Reformat the keys and encode them
    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
    
    # Transform from bytes to bytes that can be printed
    b64_encoded_key = base64.b64encode(key_secret)
    #Transform from bytes back into Unicode
    b64_encoded_key = b64_encoded_key.decode('ascii')
    
    auth_url = '{}oauth2/token'.format(base_url)
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    
    access_token = auth_resp.json()['access_token']
    
    return access_token

def getTweet(query,amount):
    access_token = createAccessToken()

    #create Query
    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)    
    }
    search_params = {
        'q': query,
        'result_type': 'mixed',
        'count': amount,
        'lang': 'en'
    }
    search_url = '{}1.1/search/tweets.json'.format(base_url)
    search_resp = requests.get(search_url, headers=search_headers, params=search_params)
    
    # Get the data from the request
    Data =  json.loads(search_resp.content)['statuses']
    tweets=[]
    for i in range(0,len(Data)):
        tweets.append(Tweet(Data[i]['user']['name'], Data[i]['text'], Data[i]['created_at']))
    # Print out the data!
    return tweets

class Tweet:
    user=text=date=''
    
    def __init__(self, user, text, date):
        dateParts = date.split(" ")
        if len(dateParts) > 3:
            dt = " on " + dateParts[0] + " " + dateParts[1] + " " + dateParts[2] + " at " + dateParts[3]
        else: 
            dt = ''
        self.user=user
        self.text=text
        self.date=dt

