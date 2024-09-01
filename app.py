# import os
# import nltk

# nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')
# nltk.data.path.append(nltk_data_path)


# import sys
# import os
# import streamlit as st
# import pandas as pd

# # Add the src directory to the path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# from data_preprocessing import preprocess_text, load_data, preprocess_data
# from model_training import train_model, predict_sentiment
# from nltk.tokenize import word_tokenize
# from src.data_preprocessing import preprocess_text, load_data, preprocess_data

# def main():
#     st.title("Sentiment Analysis Tool")
    
#     # Upload file
#     uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
#     if uploaded_file is not None:
#         df = pd.read_csv(uploaded_file)
#         df = preprocess_data(df)
        
#         st.write("Data preview:")
#         st.write(df.head())
        
#         # Train model
#         if st.button('Train Model'):
#             model = train_model(df)
#             st.write("Model trained!")
        
#         # Predict sentiment
#         user_input = st.text_area("Enter text to analyze:")
#         if st.button('Predict Sentiment'):
#             if user_input:
#                 prediction = predict_sentiment(user_input, model)
#                 st.write(f"Prediction: {prediction}")

# if __name__ == "__main__":
#     main()

























# import os
# import nltk

# # Define the path where NLTK data will be stored
# nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')

# # Ensure the NLTK data path exists
# if not os.path.exists(nltk_data_path):
#     os.makedirs(nltk_data_path)

# # Append the path to NLTK's data path
# nltk.data.path.append(nltk_data_path)

# # Download necessary NLTK resources
# nltk.download('punkt', download_dir=nltk_data_path)
# nltk.download('stopwords', download_dir=nltk_data_path)
# nltk.download('wordnet', download_dir=nltk_data_path)

# import streamlit as st
# import pandas as pd
# from data_preprocessing import preprocess_text, preprocess_data
# from model_training import train_model, predict_sentiment

# def main():
#     st.title("Sentiment Analysis Tool")
    
#     # Upload file
#     uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
#     if uploaded_file is not None:
#         df = pd.read_csv(uploaded_file)
#         df = preprocess_data(df)
        
#         st.write("Data preview:")
#         st.write(df.head())
        
#         # Train model
#         if st.button('Train Model'):
#             model = train_model(df)
#             st.write("Model trained!")
        
#         # Predict sentiment
#         user_input = st.text_area("Enter text to analyze:")
#         if st.button('Predict Sentiment'):
#             if user_input:
#                 prediction = predict_sentiment(user_input, model)
#                 st.write(f"Prediction: {prediction}")

# if __name__ == "__main__":
#     main()


























# import os
# import nltk
# import streamlit as st
# import pandas as pd
# from data_preprocessing import preprocess_text, preprocess_data
# from model_training import train_model, predict_sentiment

# # Define the path where NLTK data will be stored
# nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')

# # Ensure the NLTK data path exists
# if not os.path.exists(nltk_data_path):
#     os.makedirs(nltk_data_path)

# # Append the path to NLTK's data path
# nltk.data.path.append(nltk_data_path)

# # Ensure required NLTK resources are downloaded
# def download_nltk_resources():
#     try:
#         nltk.download('punkt', download_dir=nltk_data_path)
#         nltk.download('stopwords', download_dir=nltk_data_path)
#         nltk.download('wordnet', download_dir=nltk_data_path)
#     except Exception as e:
#         st.error(f"Error downloading NLTK resources: {e}")

# # Check if NLTK resources are already downloaded
# def check_nltk_resources():
#     resources = ['punkt', 'stopwords', 'wordnet']
#     for resource in resources:
#         try:
#             nltk.data.find(f'tokenizers/{resource}')
#         except LookupError:
#             return False
#     return True

# if not check_nltk_resources():
#     download_nltk_resources()

# def main():
#     st.title("Sentiment Analysis Tool")
    
#     # Initialize model variable
#     if 'model' not in st.session_state:
#         st.session_state.model = None

#     # Upload file
#     uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
#     if uploaded_file is not None:
#         try:
#             df = pd.read_csv(uploaded_file)
#             df = preprocess_data(df)
            
#             st.write("Data preview:")
#             st.write(df.head())
            
#             # Train model
#             if st.button('Train Model'):
#                 try:
#                     st.session_state.model = train_model(df)
#                     st.write("Model trained successfully!")
#                 except Exception as e:
#                     st.error(f"Error training model: {e}")
        
#         except Exception as e:
#             st.error(f"Error processing file: {e}")

#     # Predict sentiment
#     user_input = st.text_area("Enter text to analyze:")
#     if st.button('Predict Sentiment'):
#         if user_input:
#             if st.session_state.model is not None:
#                 try:
#                     prediction = predict_sentiment(user_input, st.session_state.model)
#                     st.write(f"Prediction: {prediction}")
#                 except Exception as e:
#                     st.error(f"Error predicting sentiment: {e}")
#             else:
#                 st.warning("Model is not trained yet. Please upload data and train the model first.")

# if __name__ == "__main__":
#     main()
















import os
import nltk

# Set the path to your NLTK data
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
