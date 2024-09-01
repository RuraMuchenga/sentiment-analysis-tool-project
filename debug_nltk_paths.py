import os
import nltk
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define the path where NLTK data will be stored
nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')

# Ensure the NLTK data path exists
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)

# Append the path to NLTK's data path
nltk.data.path.append(nltk_data_path)

# Log the NLTK data paths being used
logger.debug("NLTK data paths: %s", nltk.data.path)

# Download necessary NLTK resources
try:
    nltk.download('punkt', download_dir=nltk_data_path)
    nltk.download('stopwords', download_dir=nltk_data_path)
    nltk.download('wordnet', download_dir=nltk_data_path)
except Exception as e:
    logger.error(f"Error downloading NLTK resources: {e}")
