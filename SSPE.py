import tweepy
import csv
import numpy as np
from textblob import TextBlob
from keras.models import Sequential
from keras.layers import Dense


#Step 1 - Insert your API keys
consumer_key= '	I2YsBqxr21DCAufPPUbvaKFYA'
consumer_secret= 'U5W0GEocde1vEZsI8XlR8EG8YdptX29emN1Qz1f6lNSLPe6Xji'
access_token='	4725336534-QyWCpYeshhWT1KwU6swsPZymgoyJgpF4XqDtQzn'
access_token_secret='TBKKZ8uep7Y7Tif2yxmFPhPDKlakpaJFXWIIUlH87TGak'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Step 2 - Search for your company name on Twitter
public_tweets = api.search('google')


#Step 3 - Define a threshold for each sentiment to classify each 
#as positive or negative. If the majority of tweets you've collected are positive
#then use your neural network to predict a future price
for tweet in public_tweets:    
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    

#data collection
dates = []
prices = []
def get_data(filename):
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)
		for row in csvFileReader:
			dates.append(int(row[0].split('-')[0]))
			prices.append(float(row[1]))
	return

#Step 5 reference your CSV file here
get_data('googl.csv')

#Step 6 In this function, build your neural network model using Keras, train it, then have it predict the price 
#on a given day. We'll later print the price out to terminal.
def predict_prices(dates, prices, x):
	predicted_price = predict_price(dates, prices, 29)
	print(predicted_price)