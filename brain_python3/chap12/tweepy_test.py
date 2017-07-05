import tweepy
import datetime

consumer_key = "my consumer key"
consumer_secret = "my consumer secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = "my access token"
access_token_secret = "my access token secret"

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweet = str(datetime.datetime.now()) + ' Brain Python3 Test.'
api.update_status(status=tweet)

print("Successfully Posted.")
print()

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
