import tweepy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def tweet_price(price: str) -> None:
    # Authenticate to Twitter
    consumer_key = os.getenv("TWITTER_API_KEY")
    consumer_secret = os.getenv("TWITTER_API_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    if not all([consumer_key, consumer_key, access_token, access_token_secret]):
        raise ValueError("Missing Twitter API credentials")

    api = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

    # Create a tweet
    tweet = f"NVIDIA Current Price: {price}"
    api.create_tweet(text=tweet)