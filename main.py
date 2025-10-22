import os
import tweepy
from dotenv import load_dotenv

# --- 1. Load Environment Variables ---
# This command finds the .env file in your project and loads the
# variables from it into the environment.
load_dotenv()

# We can now safely access the token just like it was a
# system setting.
bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")

# A quick check to make sure the token was loaded.
if not bearer_token:
    raise RuntimeError("TWITTER_BEARER_TOKEN not found! Check your .env file.")

print("Successfully loaded Bearer Token.")

# --- 2. Authenticate with the Twitter API ---
# This is where we create our "client". This object is what
# we'll use to make all our requests. We pass the Bearer Token
# to it so it can prove who we are.
# 'wait_on_rate_limit=True' is a nice feature: if we make too
# many requests, it will automatically pause and retry.
try:
    client = tweepy.Client(bearer_token, wait_on_rate_limit=True)
    print("Successfully authenticated with Twitter API.")
except Exception as e:
    print(f"Error during authentication: {e}")
    exit()

# --- 3. Make Your First API Call ---
# Let's search for recent tweets.
# This query will find tweets from the last 7 days that
# contain the word "Python" and the word "developer"
# and are in English.
query = "Python developer -is:retweet lang:en"

try:
    print(f"Searching for tweets with query: '{query}'")
    
    # client.search_recent_tweets is the main function.
    # We pass it our query and ask for a max of 10 results.
    response = client.search_recent_tweets(query=query, max_results=10)

    # The 'response' object contains a 'data' field, which is
    # a list of Tweet objects.
    tweets = response.data

    if tweets:
        print(f"Success! Found {len(tweets)} tweets:")
        for tweet in tweets:
            print("---")
            print(f"ID: {tweet.id}")
            print(f"Text: {tweet.text}")
    else:
        print("No tweets found for your query.")

except tweepy.errors.TweepyException as e:
    print(f"An error occurred while searching for tweets: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")