import sys
#directory with the api.py file
sys.path.append('c:/Users/user/Documents/OpenAi/twitter-tool/twitter-tool/src')
import unittest
import main

class TestMain(unittest.TestCase):
    def test_main(self):
        # Call the main() function
        main.main()
        # Add any additional tests or assertions to verify the correct behavior of the main() function
