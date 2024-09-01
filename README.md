# Sentiment Analysis Tool

By: Ruramai Muchenga | https://sentiment-analysis-tool-project.streamlit.app/

This project is a sentiment analysis tool that classifies text data into positive, negative, or neutral sentiments. The application uses natural language processing (NLP) techniques and machine learning models to perform sentiment classification. The tool is implemented using Python, NLTK, and Streamlit for the user interface.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)


## Project Overview

The goal of this project is to analyze the sentiment of text data, such as tweets or customer reviews. By using NLP techniques, the tool can help businesses understand customer opinions and improve customer experience by tailoring responses based on feedback.

## Features

- Preprocessing of text data (removal of stopwords, lemmatization, etc.)
- Tokenization and negation handling
- Sentiment classification using machine learning models
- Streamlit-based user interface for easy interaction
- Visualization of sentiment analysis results

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/RuraMuchenga/sentiment-analysis-tool.git
    cd sentiment-analysis-tool
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Download necessary NLTK data:**

    Ensure that the `nltk_data` folder is located in the project directory and includes required datasets (`punkt`, `stopwords`, `wordnet`). If the folder is missing, run the setup script:

    ```bash
    python setup.py
    ```

## Usage

1. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

2. **Open your web browser and navigate to:**

    ```
    http://localhost:8502/
    ```

3. **Interact with the app:**

    - Upload a text file or manually enter text to analyze.
    - View the sentiment analysis results and corresponding visualizations.

## Project Structure

The project is organized into the following directories and files:

### Description:

- **`nltk_data/`**: Contains the necessary NLTK datasets and models used for text processing. This includes the `punkt` tokenizer models.

- **`src/`**: The source code directory.
  - **`data_preprocessing.py`**: Handles the preprocessing of text data, including tokenization, stopword removal, and lemmatization.
  - **`model_training.py`**: Contains code for training the sentiment analysis models.
  - **`__init__.py`**: Initialization file to make the `src` directory a package.

- **`dashboard/`**: Contains the Streamlit app code.
  - **`app.py`**: Main script for running the Streamlit app that provides the user interface for sentiment analysis.

- **`setup.py`**: A script for downloading and setting up necessary NLTK resources.

- **`requirements.txt`**: Lists all the Python packages required for the project.

- **`README.md`**: Documentation file providing an overview of the project, setup instructions, and usage guidelines.

Feel free to adjust this structure based on any additional directories or files you may have!




## Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository and create a pull request with your changes. Additionaly you can also email me at ruramaimuchenga@gmail.com.

1. Fork the project
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request







