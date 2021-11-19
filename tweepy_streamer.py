from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
class TwitterClient():
	def __init__(self, twitter_user=None):
		self.auth = TwitterAuthenticator().authenticate_twitter_app()
		self.twitter_client = API(self.auth)
		
		self.twitter_user=twitter_user
	def get_twitter_client_api(self):
		return self.twitter_client
		
		
	def get_user_timeline_tweets(self, num_tweets):
		tweets = []
		for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
			tweets.append(tweet)
		return tweets
			
	def get_friend_list(self, num_friends):
		friend_list = []
		for friend in Cursor(self.twitter_client.friends).items(num_friends):
			friend_list.append(friend)
		return friend_list
	
	def get_home_timeline_tweets(self, num_tweets):
		home_timeline_tweets=[]
		for tweet in Cursor(self.twitter_client.home_timeline).items(num_tweets):
			home_timeline_tweets.append(tweet)
		return home_timeline_tweets	
		
	
class TwitterAuthenticator():
	def authenticate_twitter_app(self):
		auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
		auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
		return auth

class TwitterStreamer():

	def __init__(self):
		self.twitter_authenticator = TwitterAuthenticator()
		
	def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
		#handles twitter authentication and the connection to the twitter streaming api.
		listener = TwitterListener(fetched_tweets_filename)
		auth = self.twitter_authenticator.authenticate_twitter_app()
		stream = Stream(auth, listener)
		
		stream.filter(track=hash_tag_list)
		
class TwitterListener(StreamListener):

	def __init__(self, fetched_tweets_filename):
		self.fetched_tweets_filename=fetched_tweets_filename
		
	def on_data(self, data):
		try:
			print(data)
			with open(self.fetched_tweets_filename, 'a') as tf:
				tf.write(data)
			return True
		except BaseException as e:
			print("error_on_data %s" % str(e))
		return true
		
	def on_error(self, status):
		if status == 420:
			return False
		print(status)
class TweetAnalyzer():
	def tweets_to_data_frame(self, tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet'])
		
		df['id'] = np.array([tweet.id for tweet in tweets])
		df['len'] = np.array([len(tweet.text) for tweet in tweets])
		df['date'] = np.array([tweet.created_at for tweet in tweets])
		df['source'] = np.array([tweet.source for tweet in tweets])
		df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
		df['retweet'] = np.array([tweet.retweet_count for tweet in tweets])
		#df['location'] = np.array([tweet.location for tweet in tweets])
		#df['lat'] = np.array([tweet.lat for tweet in tweets])
		#df['long'] = np.array([tweet.long for tweet in tweets])
		return df

if __name__ == "__main__":
	twitter_client = TwitterClient()
	tweet_analyzer = TweetAnalyzer()
	api = twitter_client.get_twitter_client_api()
	
	tweets = api.user_timeline(screen_name="elonmusk", count=200)
	#tweets = api.user_timeline(screen_name="JohnBro41510468", count=200)
	
	df = tweet_analyzer.tweets_to_data_frame(tweets)
	
	#print(df.head(200))
	print(np.mean(df['len']))
	
	print(np.max(df['likes']))
	
	print(np.max(df['retweet']))
	
	#time_likes = pd.Series(data=df['likes'].values, index=df['date'])
	#time_likes.plot(figsize=(16, 4), color='r')
	#plt.show()
	
	#time_retweets = pd.Series(data=df['retweet'].values, index=df['date'])
	#time_retweets.plot(figsize=(16, 4), color='b')
	#plt.show()
	
	time_likes = pd.Series(data=df['likes'].values, index=df['date'])
	time_likes.plot(figsize=(16, 4), label="likes", legend=True)
	
	time_retweets = pd.Series(data=df['retweet'].values, index=df['date'])
	time_retweets.plot(figsize=(16, 4), label="retweets", legend=True)
	
	plt.show()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	