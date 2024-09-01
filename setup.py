import os
import nltk

# Define the exact path to your local nltk_data directory
nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')

# Append the path to NLTK's data path
nltk.data.path.append(nltk_data_path)

# Download necessary NLTK resources if not already present
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)
nltk.download('wordnet', download_dir=nltk_data_path)
