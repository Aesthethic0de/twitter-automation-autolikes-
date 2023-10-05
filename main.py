import tweepy

# Authenticate to Twitter (Replace with your API keys)
auth = tweepy.OAuth1UserHandler(
    consumer_key="YOUR_CONSUMER_KEY",
    consumer_secret="YOUR_CONSUMER_SECRET",
    access_token="YOUR_ACCESS_TOKEN",
    access_token_secret="YOUR_ACCESS_TOKEN_SECRET",
)

api = tweepy.API(auth)

# Auto-like tweets with hashtag #PythonRocks
for tweet in tweepy.Cursor(api.search_tweets, q="#PythonRocks", lang="en").items(5):
    try:
        print(f"Liking tweet by @{tweet.user.screen_name}")
        tweet.favorite()
    except Exception as e:
        print(str(e))
