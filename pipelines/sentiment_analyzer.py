from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="ProsusAI/finbert")

def analyze_sentiment(texts):
    if not texts:
        return 50  # Neutral
    results = sentiment_pipeline(texts)
    scores = [1 if r['label'] == 'positive' else -1 if r['label'] == 'negative' else 0 for r in results]
    return sum(scores) / len(scores) * 50 + 50  # Scale from 0 to 100
