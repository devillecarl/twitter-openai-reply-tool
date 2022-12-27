import api as api_module
import config
import openai_client
import ui
import requests_oauthlib as auth 

def select_tweet(tweets):
    """
    Selects a tweet from the provided list of tweets that has more than 100 comments.
    Returns the selected tweet object.
    """
    for tweet in tweets:
        if tweet.favorite_count > 100:
            return tweet
    return None

def main():
    # Prompt the user for the required arguments
    args = ui.prompt_arguments()

    # Authenticate with the Twitter API
    api = api_module.authenticate_twitter_api()

    # Get the most trending topics on Twitter
    trends = api_module.get_trending_topics(api)


    # Search for tweets related to the specified query
    tweets = api_module.search_tweets(api, args["query"], args["exclude"])

    # Select a tweet with more than 100 comments
    tweet = select_tweet(tweets)
    if tweet:
        # Use the ChatGPT API to generate a joke based on the selected tweet
        prompt = "Write a dark humor joke based on the following tweet: " + tweet.text
        joke = openai_client.generate_joke(prompt)

        # Send the generated joke as a reply to the selected tweet
        api_module.send_reply(api, tweet, joke)
    else:
        print("No tweets with more than 100 comments were found.")

if __name__ == "__main__":
    main()