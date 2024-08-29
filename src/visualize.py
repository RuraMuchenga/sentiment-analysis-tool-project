# src/visualize.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_sentiment_distribution(df):
    plt.figure(figsize=(6,4))
    sns.countplot(df['sentiment'])
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.title('Sentiment Distribution')
    plt.show()
