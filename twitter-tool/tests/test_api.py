import sys
#directory with the api.py file
sys.path.append('c:/Users/user/Documents/OpenAi/twitter-tool/twitter-tool/src')
#sys.path.append('/')
import unittest
import api



class TestApi(unittest.TestCase):
    def test_authenticate_twitter_api(self):
        # Call the authenticate_twitter_api() function
        api_obj = api.authenticate_twitter_api()
        # Check if the returned object is an authenticated API object
        self.assertIsInstance(api_obj, tweepy.API)
        
    def test_get_trending_topics(self):
        # Call the authenticate_twitter_api() function to get an authenticated API object
        api_obj = api.authenticate_twitter_api()
        # Call the get_trending_topics() function
        trends = api.get_trending_topics(api_obj)
        # Check if the returned list is not empty
        self.assertTrue(trends)
        
    def test_search_tweets(self):
        # Call the authenticate_twitter_api() function to get an authenticated API object
        api_obj = api.authenticate_twitter_api()
        # Call the search_tweets() function with a sample query
        tweets = api.search_tweets(api_obj, "test query")
        # Check if the returned list is not empty
        self.assertTrue(tweets)
        
    def test_reply_to_tweet(self):
        # Call the authenticate_twitter_api() function to get an authenticated API object
        api_obj = api.authenticate_twitter_api()
        # Create a sample tweet object
        tweet = tweepy.Status()
        tweet.id = 12345
        # Call the reply_to_tweet() function with the sample tweet object and a sample reply text
        api.reply_to_tweet(api_obj, tweet, "Sample reply text")
        # Check if the tweet has been successfully replied to by checking the reply count
        self.assertEqual(tweet.reply_count, 1)
