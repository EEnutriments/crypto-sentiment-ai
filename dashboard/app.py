import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from pipelines.reddit_scraper import fetch_reddit_posts
from pipelines.sentiment_analyzer import analyze_sentiment
from utils.price_tracker import get_btc_price

st.set_page_config(page_title="Crypto Sentiment AI", layout="wide")
st.title("🧠 Crypto Sentiment AI")

btc_price = get_btc_price()
posts = fetch_reddit_posts()
score = analyze_sentiment(posts)

st.metric("💰 Bitcoin Price", f"${btc_price}")
st.metric("📊 Sentiment Score", f"{round(score, 2)} / 100")
classification = "😱 Fear" if score < 40 else "😐 Neutral" if score < 60 else "🚀 Greed"
st.success(f"Sentiment Classification: **{classification}**")
