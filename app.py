
import os
import nltk


nltk_data_path = 'C:\\Users\\ruram\\Sentiment-Analysis-Tool-Project\\nltk_data'
nltk.data.path.append(nltk_data_path)

# Attempt to download resources if they aren't already present
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)
nltk.download('wordnet', download_dir=nltk_data_path)
nltk.download('omw-1.4', download_dir=nltk_data_path)

import streamlit as st
import pandas as pd
from data_preprocessing import preprocess_text, preprocess_data
from model_training import train_model, predict_sentiment

def main():
    st.title("Sentiment Analysis Tool")

    # File upload functionality
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df = preprocess_data(df)

        st.write("Data preview:")
        st.write(df.head())

        # Model training
        if st.button('Train Model'):
            model = train_model(df)
            st.write("Model trained!")

        # Sentiment prediction
        user_input = st.text_area("Enter text to analyze:")
        if st.button('Predict Sentiment'):
            if user_input:
                prediction = predict_sentiment(user_input, model)
                st.write(f"Prediction: {prediction}")

if __name__ == "__main__":
    main()
