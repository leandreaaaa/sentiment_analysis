# Sentiment Analysis on Movie Reviews

This Sentiment analysis tool helps to classify movie reviews into positive or negative categories

The IMDB dataset from huggingfaces will be utilised for this classification

## Instructions

1. Clone the repository:
    ```bash
    git clone <https://github.com/leandreaaaa/sentiment_analysis>
    cd sentiment-analysis-movie-reviews
    ```

2. Setting up the virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Download the IMDB dataset:
    ```bash
    python download_dataset.py
    ```

5. Run the sentiment analysis script:
    ```bash
    python sentiment_analysis.py
    ```