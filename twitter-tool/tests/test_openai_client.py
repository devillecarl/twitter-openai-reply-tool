import sys
#directory with the api.py file
sys.path.append('c:/Users/user/Documents/OpenAi/twitter-tool/twitter-tool/src')
import unittest
import openai_client

class TestOpenaiClient(unittest.TestCase):
    def test_generate_joke(self):
        # Call the generate_joke() function with a sample prompt
        joke = openai_client.generate_joke("Write a joke about a penguin")
        # Check if the returned joke is a string
        self.assertIsInstance(joke, str)
        # Check if the returned joke is not empty
        self.assertTrue(joke)
        
    def test_send_message(self):
        # Call the send_message() function with a sample recipient and message
        openai_client.send_message("recipient@example.com", "Sample message")
        # Add any additional tests or assertions to verify the correct behavior of the send_message() function
