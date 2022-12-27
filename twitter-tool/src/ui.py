import config
import argparse

def parse_arguments():
    """
    Parses command-line arguments for the Twitter tool.
    Returns a dictionary of parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--exclude", help="Keywords to exclude from the search results.")
    return vars(parser.parse_arguments())

def prompt_arguments():
    """
    Prompts the user for the required arguments for the Twitter tool.
    Returns a dictionary of the entered arguments.
    """
    # Check if the configuration file exists
    if config.exists():
        # Prompt the user to use the saved configuration or enter new values
        use_saved = input("Use saved configuration? (y/n) ")
        if use_saved.lower() == "y":
            # Load the saved configuration
            return config.load()
    # Prompt the user to enter the required arguments
    query = input("Enter a search query: ")
    twitter_api_key = input("Enter your Twitter API key: ")
    twitter_api_secret_key = input("Enter your Twitter API secret key: ")
    twitter_access_token = input("Enter your Twitter access token: ")
    twitter_access_token_secret = input("Enter your Twitter access token secret: ")
    bearer_token = input("Enter your Twitter bearer token: ")
    openai_api_key = input("Enter your OpenAI API key: ")
    frequency = input("Enter the frequency (in minutes) at which to run the tool: ")
    start_time = input("Enter the time (in hours) at which to start running the tool (0-23): ")
    end_time = input("Enter the time (in hours) at which to stop running the tool (0-23): ")
    max_tweets = input("Enter the maximum number of tweets to send per run of the tool: ")
    humor = input("Enter the type of humor to generate (e.g. dark, absurd, etc.): ")
# Save the entered arguments to the configuration file
    config.save({
        "query": query,
        "twitter_api_key": twitter_api_key,
        "twitter_api_secret_key": twitter_api_secret_key,
        "twitter_access_token": twitter_access_token,
        "twitter_access_token_secret": twitter_access_token_secret,
        "bearer_token": bearer_token,
        "openai_api_key": openai_api_key,
        "frequency": frequency,
        "start_time": start_time,
        "end_time": end_time,
        "max_tweets": max_tweets,
        "humor": humor,
    })
    return {
        "query": query,
        "twitter_api_key": twitter_api_key,
        "twitter_api_secret_key": twitter_api_secret_key,
        "twitter_access_token": twitter_access_token,
        "twitter_access_token_secret": twitter_access_token_secret,
        "bearer_token": bearer_token,
        "openai_api_key": openai_api_key,
        "frequency": frequency,
        "start_time": start_time,
        "end_time": end_time,
        "max_tweets": max_tweets,
        "humor": humor,
    }

