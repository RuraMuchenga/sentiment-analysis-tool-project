import nltk

# Function to download necessary NLTK resources
def download_nltk_resources():
    nltk.download('punkt')  # Includes the required 'punkt_tab'
    nltk.download('stopwords')
    nltk.download('wordnet')

download_nltk_resources()
