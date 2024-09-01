import shutil
import os
import nltk

# Define the path where NLTK data is stored
nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')

# Remove existing NLTK data directory
if os.path.exists(nltk_data_path):
    shutil.rmtree(nltk_data_path)

# Create a new NLTK data directory
os.makedirs(nltk_data_path)

# Append the path to NLTK's data path
nltk.data.path.append(nltk_data_path)

# Download necessary NLTK resources
try:
    nltk.download('punkt', download_dir=nltk_data_path)
    nltk.download('stopwords', download_dir=nltk_data_path)
    nltk.download('wordnet', download_dir=nltk_data_path)
    nltk.download('omw-1.4', download_dir=nltk_data_path)
except Exception as e:
    print(f"Error downloading NLTK resources: {e}")
