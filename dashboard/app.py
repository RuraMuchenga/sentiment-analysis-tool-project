

# import sys
# import os
# import streamlit as st
# import pandas as pd

# # Add the src directory to the path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# from data_preprocessing import preprocess_text, preprocess_data
# from model_training import train_model, predict_sentiment

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
#                     st.write(f"Error training model: {e}")
        
#         except Exception as e:
#             st.write(f"Error processing file: {e}")

#     # Predict sentiment
#     user_input = st.text_area("Enter text to analyze:")
#     if st.button('Predict Sentiment'):
#         if user_input:
#             if st.session_state.model is not None:
#                 try:
#                     prediction = predict_sentiment(user_input, st.session_state.model)
#                     st.write(f"Prediction: {prediction}")
#                 except Exception as e:
#                     st.write(f"Error predicting sentiment: {e}")
#             else:
#                 st.write("Model is not trained yet. Please upload data and train the model first.")

# if __name__ == "__main__":
#     main()
















# import sys
# import os
# import streamlit as st
# import pandas as pd
# import nltk
# from nltk.corpus import stopwords

# # Ensure required NLTK resources are downloaded
# try:
#     nltk.download('punkt')
#     nltk.download('stopwords')
#     nltk.download('wordnet')
# except Exception as e:
#     st.error(f"Error downloading NLTK resources: {e}")

# # Set up NLTK stop words
# stop_words = set(stopwords.words('english'))

# # Add the src directory to the path
# src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
# sys.path.insert(0, src_path)

# try:
#     from data_preprocessing import preprocess_text, preprocess_data
#     from model_training import train_model, predict_sentiment
# except ImportError as e:
#     st.error(f"Error importing modules: {e}")
#     st.stop()

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































import sys
import os
import streamlit as st
import pandas as pd
import nltk
from nltk.corpus import stopwords

# Ensure the NLTK data path is correctly set
nltk_data_path = os.path.join(os.path.dirname(__file__), '..', 'nltk_data')
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)

nltk.data.path.append(nltk_data_path)

# Ensure required NLTK resources are downloaded
try:
    nltk.download('punkt', download_dir=nltk_data_path)
    nltk.download('stopwords', download_dir=nltk_data_path)
    nltk.download('wordnet', download_dir=nltk_data_path)
    nltk.download('omw-1.4', download_dir=nltk_data_path)
except Exception as e:
    st.error(f"Error downloading NLTK resources: {e}")

# Set up NLTK stop words
stop_words = set(stopwords.words('english'))

# Add the src directory to the path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, src_path)

try:
    from data_preprocessing import preprocess_text, preprocess_data
    from model_training import train_model, predict_sentiment
except ImportError as e:
    st.error(f"Error importing modules: {e}")
    st.stop()

def main():
    st.title("Sentiment Analysis Tool")
    
    # Initialize model variable
    if 'model' not in st.session_state:
        st.session_state.model = None

    # Upload file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            df = preprocess_data(df)
            
            st.write("Data preview:")
            st.write(df.head())
            
            # Train model
            if st.button('Train Model'):
                try:
                    st.session_state.model = train_model(df)
                    st.write("Model trained successfully!")
                except Exception as e:
                    st.error(f"Error training model: {e}")
        
        except Exception as e:
            st.error(f"Error processing file: {e}")

    # Predict sentiment
    user_input = st.text_area("Enter text to analyze:")
    if st.button('Predict Sentiment'):
        if user_input:
            if st.session_state.model is not None:
                try:
                    prediction = predict_sentiment(user_input, st.session_state.model)
                    st.write(f"Prediction: {prediction}")
                except Exception as e:
                    st.error(f"Error predicting sentiment: {e}")
            else:
                st.warning("Model is not trained yet. Please upload data and train the model first.")

if __name__ == "__main__":
    main()
