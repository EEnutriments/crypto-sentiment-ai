import praw
import streamlit as st

def fetch_reddit_posts(subreddit="CryptoCurrency", limit=50):
    reddit = praw.Reddit(
        client_id=st.secrets["REDDIT_CLIENT_ID"],
        client_secret=st.secrets["REDDIT_SECRET"],
        user_agent="CryptoSentimentBot"
    )
    posts = reddit.subreddit(subreddit).hot(limit=limit)
    return [post.title + " " + post.selftext for post in posts]
