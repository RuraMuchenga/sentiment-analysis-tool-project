import os
import nltk


nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')


nltk.data.path.append(nltk_data_path)


nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)
nltk.download('wordnet', download_dir=nltk_data_path)
