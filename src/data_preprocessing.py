# import pandas as pd
# import re
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer

# import os
# import nltk

# nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')
# nltk.data.path.append(nltk_data_path)


# # Download necessary NLTK resources
# # nltk.download('punkt')
# # nltk.download('stopwords')
# # nltk.download('wordnet')

# # Load stopwords once
# stop_words = set(stopwords.words('english'))

# def preprocess_text(text):
#     # Handle negations (e.g., "not good" becomes "not_good")
#     text = re.sub(r"\bnot\s+\w+", lambda match: match.group(0).replace(" ", "_"), text)
    
#     # Remove special characters and convert to lower case
#     text = re.sub(r'[^a-zA-Z\s_]', '', text)  # Keep only letters, spaces, and underscores
#     text = text.lower()
#     text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space

#     # Tokenize and remove stopwords
#     tokens = word_tokenize(text)
#     tokens = [word for word in tokens if word not in stop_words]

#     # Lemmatize
#     lemmatizer = WordNetLemmatizer()
#     tokens = [lemmatizer.lemmatize(word) for word in tokens]

#     return ' '.join(tokens)

# def preprocess_data(df):
#     # Ensure 'text' and 'sentiment' columns are present
#     if 'text' not in df.columns or 'sentiment' not in df.columns:
#         raise ValueError("DataFrame must contain 'text' and 'sentiment' columns.")

#     # Apply preprocessing
#     df['cleaned_text'] = df['text'].apply(preprocess_text)

#     return df


















import os
import nltk

# Ensure the NLTK data path is correctly set
nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')
nltk.data.path.append(nltk_data_path)

# Force download of necessary NLTK resources
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)
nltk.download('wordnet', download_dir=nltk_data_path)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd
import re

# Load stopwords once
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Handle negations (e.g., "not good" becomes "not_good")
    text = re.sub(r"\bnot\s+\w+", lambda match: match.group(0).replace(" ", "_"), text)
    
    # Remove special characters and convert to lower case
    text = re.sub(r'[^a-zA-Z\s_]', '', text)  # Keep only letters, spaces, and underscores
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space

    # Tokenize and remove stopwords
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return ' '.join(tokens)

def preprocess_data(df):
    # Ensure 'text' and 'sentiment' columns are present
    if 'text' not in df.columns or 'sentiment' not in df.columns:
        raise ValueError("DataFrame must contain 'text' and 'sentiment' columns.")

    # Apply preprocessing
    df['cleaned_text'] = df['text'].apply(preprocess_text)

    return df
