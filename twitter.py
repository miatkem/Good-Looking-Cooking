import os
import json
import requests
import base64

#pull keys from os.environ and initialize twitter url
keys = {}
keys['CONSUMER_KEY'] = os.environ['TWITTER_API_KEY']
keys['CONSUMER_SECRET'] = os.environ['TWITTER_API_KEY_SECRET']
keys['ACCESS_TOKEN'] = os.environ['TWITTER_ACCESS_TOKEN']
keys['ACCESS_SECRET'] = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
url = 'https://api.twitter.com/'

#function to create request access token
# NOTE: Credits of this function got to https://christophegaron.com/scrape-tweets-python/
def createAccessToken():
    #Define your keys from the developer portal
    client_key = keys['CONSUMER_KEY']
    client_secret = keys['CONSUMER_SECRET']
    
    #Reformat the keys and encode them
    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
    
    # Transform from bytes to bytes that can be printed
    b64_encoded_key = base64.b64encode(key_secret)
    
    #Transform from bytes back into Unicode
    b64_encoded_key = b64_encoded_key.decode('ascii')
    
    #create headers and auth data
    auth_url = '{}oauth2/token'.format(url)
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }
    
    #generate and return access token
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    access_token = auth_resp.json()['access_token']
    return access_token

#Generate tweets given a query, the amount of results, and optionally some backup keywords
def getTweet(query,amount, keywords=None):
    
    #create requests access token
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
    search_url = '{}1.1/search/tweets.json'.format(url)
    
    #make request to twitter
    search_resp = requests.get(search_url, headers=search_headers, params=search_params)
    
    # Get the data from the response
    Data =  json.loads(search_resp.content)['statuses']
    tweets=[]
    for i in range(0,len(Data)): #loop through tweets and create tweet objects with needed data
        tweets.append(Tweet(Data[i]['user']['name'], Data[i]['text'], Data[i]['created_at']))
        
    #IF: no tweets were found with the query
    #THEN: loop through keywords until one gets a response with a tweet
    if len(tweets) < 1 and keywords != None:
        for keyword in keywords:
            tweets = getTweet(keyword,amount)
            if len(tweets) > 1:
                return tweets
    
    return tweets

#Tweet object - holds user, text, and date so that tweets can be moved around in a more
#               light weight data structure in flask
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

