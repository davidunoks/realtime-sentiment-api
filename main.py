import os
import tweepy
from dotenv import load_dotenv
from transformers import pipeline  # NEW: Import the 'pipeline' function

# --- 1. Load Environment Variables ---
load_dotenv()
bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")

if not bearer_token:
    raise RuntimeError("TWITTER_BEARER_TOKEN not found! Check your .env file.")

print("Successfully loaded Bearer Token.")

# --- NEW: 2. Load the Sentiment Analysis Model ---
# This is the "magic". We're loading a pre-trained model.
# The 'pipeline' function from Hugging Face is the easiest way to do this.
# It handles all the complex stuff (tokenization, model inference) for us.
# The model 'cardiffnlp/twitter-roberta-base-sentiment-latest' is
# specifically trained for sentiment on Twitter data.
print("Loading sentiment analysis model... (This may take a moment on first run)")
# We'll use 'text-classification' as the task
sentiment_pipeline = pipeline(
    task="sentiment-analysis", 
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)
print("Sentiment model loaded successfully.")


# --- 3. Authenticate with the Twitter API ---
try:
    client = tweepy.Client(bearer_token, wait_on_rate_limit=True)
    print("Successfully authenticated with Twitter API.")
except Exception as e:
    print(f"Error during authentication: {e}")
    exit()

# --- 4. Make Your API Call ---
# Let's search for a more interesting topic this time.
query = "Tesla -is:retweet lang:en"

try:
    print(f"Searching for tweets with query: '{query}'")
    response = client.search_recent_tweets(query=query, max_results=10)
    tweets = response.data

    if tweets:
        print(f"Success! Found {len(tweets)} tweets. Analyzing sentiment...")
        
        for tweet in tweets:
            print("---")
            print(f"Text: {tweet.text}")
            
            # --- NEW: 5. Analyze the Sentiment ---
            # We pass the raw tweet text directly to the model.
            try:
                sentiment_result = sentiment_pipeline(tweet.text)
                
                # The model returns a list, so we get the first (and only) item.
                # It looks like: [{'label': 'positive', 'score': 0.98}]
                label = sentiment_result[0]['label']
                score = sentiment_result[0]['score']
                
                print(f"Sentiment: {label} (Score: {score:.4f})")
                
            except Exception as e:
                print(f"Error during sentiment analysis: {e}")

    else:
        print("No tweets found for your query.")

except tweepy.errors.TweepyException as e:
    print(f"An error occurred while searching for tweets: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")