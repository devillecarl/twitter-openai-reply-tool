import tweepy
import base64
import requests
import requests_oauthlib
import json 
import config
from tweepy import API

def authenticate_twitter_api():
    """
    Authenticates the Twitter API using the saved configuration details.
    Returns an authenticated Twitter API object.
    """
    # Load the saved configuration
    config_data = config.load()
    # Extract the required fields from the configuration data
    api_key = config_data["twitter_api_key"]
    api_secret_key = config_data["twitter_api_secret_key"]
    access_token = config_data["twitter_access_token"]
    access_token_secret = config_data["twitter_access_token_secret"]
    # Initialize the OAuth1UserHandler object with the authentication details
    auth = tweepy.OAuth1UserHandler(
        api_key,
        api_secret_key,
        access_token,
        access_token_secret
    )
    # Create an API object using the OAuth1UserHandler object
    api = tweepy.API(auth)
    return api



def get_trending_topics(api):
    """
    Gets the trending topics for the specified location.
    Returns a list of trend objects.
    """
    # Get the trending topics using the API.get_place_trends method
    trends = api.get_place_trends(id=1)
    # Check if the trends list is empty
    if not trends:
        print("No trending topics were found.")
        return []

    return trends


def search_tweets(api, query, exclude=None):
    """
    Searches for tweets related to the specified query, excluding any tweets that contain the specified exclude keywords.
    Returns a list of tweet objects.
    """
    results = api.search(q=query, lang="en", count=100)
    tweets = [tweet for tweet in results if not any(word in tweet.text for word in exclude)]
    return tweets

def reply_to_tweet(api, tweet, reply):
    """
    Replies to the specified tweet with the specified reply text.
    """
    api.update_status(status=reply, in_reply_to_status_id=tweet.id)