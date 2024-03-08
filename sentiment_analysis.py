from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
from datasets import load_dataset
import textwrap

# Define the model name
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# Load the model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a sentiment analysis pipeline
sentiment_analysis_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Load the IMDB dataset
dataset = load_dataset("imdb")

# Function to process and classify reviews
def process_review(review):
    try:
        # Tokenize the review
        tokens = tokenizer(review, truncation=True, max_length=512, return_tensors="pt")

        # Check if tokens are empty (sometimes truncation results in empty tokens)
        if "input_ids" not in tokens or tokens["input_ids"].numel() == 0:
            print(f"Review is too short after truncation: {review}")
            return

        # Classify the tokenized review
        result = sentiment_analysis_pipeline(review)

        # Prints original review, predicted sentiment label, confidence level
        print(f"Review: {review}")
        print(f"Sentiment: {result[0]['label']} ({result[0]['score']:.4f})")
        print("=" * 50)
    except Exception as e:
        print(f"Error processing review: {e}")
        print("=" * 50)

# Iterate through the reviews in the IMDB dataset
for example in dataset['test']:
    review = example['text']
    process_review(review)
