import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

def train_model(df):
    X = df['cleaned_text']
    y = df['sentiment']
    
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X, y)
    return model

def predict_sentiment(text, model):
    prediction = model.predict([text])
    return prediction[0]
