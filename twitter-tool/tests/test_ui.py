import sys
#directory with the api.py file
sys.path.append('c:/Users/user/Documents/OpenAi/twitter-tool/twitter-tool/src')
import unittest
import ui

class TestUi(unittest.TestCase):
    def test_prompt_arguments(self):
        # Call the prompt_arguments() function
        args = ui.prompt_arguments()
        # Check if the returned dictionary contains the required keys
        self.assertTrue("query" in args)
        self.assertTrue("exclude" in args)
        
    def test_display_trending_topics(self):
        # Create a sample list of trend objects
        trends = [tweepy.Trend(name="Trend 1"), tweepy.Trend(name="Trend 2")]
        # Call the display_
