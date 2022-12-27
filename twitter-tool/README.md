# Twitter Reply Bot Tool with chatgpt output
This tool allows you to search for tweets related to a specific query, select a tweet with more than 100 comments, and generate a joke based on the selected tweet using the OpenAI ChatGPT API. The generated joke is then sent as a reply to the selected tweet.

## Requirements
- Python 3.6 or higher
- Tweepy library (pip install tweepy)
- Requests-OAuthlib library (pip install requests-oauthlib)
## Setup
Clone the repository and navigate to the project directory:
```
git clone https://github.com/USERNAME/twitter-tool.git
cd twitter-tool
```
Create a virtual environment and activate it:
```
python -m venv env
source env/bin/activate
```
Install the required libraries:
```
pip install -r requirements.txt
```
Create a configuration file by copying the example file and adding your own API keys and access tokens:
```
cp config.example.py config.py
```
Run the main script:
```
python src/main.py
```
## Usage
When you run the main script, you will be prompted to enter the following arguments:

1. query: The search query for tweets.
2. exclude: A list of keywords to exclude from the search results.

The tool will then search for tweets related to the specified query, excluding any tweets that contain the specified exclude keywords. It will select a tweet with more than 100 comments and use the OpenAI ChatGPT API to generate a joke based on the selected tweet. The generated joke will be sent as a reply to the selected tweet.

If no tweets with more than 100 comments are found, a message indicating that no tweets were found will be printed.

## Contributing
If you would like to contribute to the project, please follow the steps below:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make the necessary changes and commit them.
4. Push the changes to your fork and create a pull request.
## License
This project is licensed under the MIT License - see the LICENSE file for details.