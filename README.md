# Sentiment Analysis on Movie Reviews

This project uses the Hugging Face Transformers library to perform sentiment analysis on movie reviews.

## Instructions

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd sentiment-analysis-movie-reviews
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
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

## Notes

- Make sure to replace `<repository_url>` with the actual URL of your Git repository.
- Customize the reviews in `sentiment_analysis.py` as needed.
