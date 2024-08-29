import nltk
nltk.download('punkt')

import sys
import os
import streamlit as st
import pandas as pd

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from data_preprocessing import preprocess_text, load_data, preprocess_data
from model_training import train_model, predict_sentiment
from nltk.tokenize import word_tokenize
from src.data_preprocessing import preprocess_text, load_data, preprocess_data

def main():
    st.title("Sentiment Analysis Tool")
    
    # Upload file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df = preprocess_data(df)
        
        st.write("Data preview:")
        st.write(df.head())
        
        # Train model
        if st.button('Train Model'):
            model = train_model(df)
            st.write("Model trained!")
        
        # Predict sentiment
        user_input = st.text_area("Enter text to analyze:")
        if st.button('Predict Sentiment'):
            if user_input:
                prediction = predict_sentiment(user_input, model)
                st.write(f"Prediction: {prediction}")

if __name__ == "__main__":
    main()
