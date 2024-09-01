import os
import nltk
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')


if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)


nltk.data.path.append(nltk_data_path)


logger.debug("NLTK data paths: %s", nltk.data.path)

# Download necessary NLTK resources
try:
    nltk.download('punkt', download_dir=nltk_data_path)
    nltk.download('stopwords', download_dir=nltk_data_path)
    nltk.download('wordnet', download_dir=nltk_data_path)
except Exception as e:
    logger.error(f"Error downloading NLTK resources: {e}")
print(nltk.data.path)
