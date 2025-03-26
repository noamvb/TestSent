import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re

class SentimentAnalyzer:
    def __init__(self):
        # Download required NLTK data (only needed first time)
        try:
            nltk.data.find('vader_lexicon')
        except LookupError:
            nltk.download('vader_lexicon')
        
        # Initialize the VADER sentiment analyzer
        self.analyzer = SentimentIntensityAnalyzer()
    
    def clean_text(self, text):
        """Clean and preprocess text for analysis"""
        # Convert to lowercase
        text = text.lower()
        # Remove special characters and extra spaces
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def analyze(self, text):
        """Analyze the sentiment of the given text"""
        # Clean the text
        cleaned_text = self.clean_text(text)
        
        # Get sentiment scores
        scores = self.analyzer.polarity_scores(cleaned_text)
        
        # Determine sentiment category
        if scores['compound'] >= 0.05:
            sentiment = "Positive"
        elif scores['compound'] <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        
        # Return results
        return {
            "text": text,
            "cleaned_text": cleaned_text,
            "sentiment": sentiment,
            "scores": {
                "positive": scores["pos"],
                "neutral": scores["neu"],
                "negative": scores["neg"],
                "compound": scores["compound"]
            }
        }
    
    def get_emoji(self, sentiment):
        """Return an emoji representing the sentiment"""
        if sentiment == "Positive":
            return "😃"
        elif sentiment == "Negative":
            return "😔"
        else:
            return "😐"