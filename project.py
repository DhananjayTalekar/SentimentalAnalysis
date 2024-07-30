import requests
from bs4 import BeautifulSoup
import pandas as pd
from nltk.corpus import stopwords
from textblob import TextBlob
import nltk
import matplotlib.pyplot as plt
import seaborn as sns

nltk.download('stopwords')

# Web Scraping Customer Reviews
url = "https://www.amazon.in/product-reviews/B0BT9CXXXX/ref=cm_cr_othr_mb_show_all_top?ie=UTF8&reviewerType=all_reviews"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

reviews = []
for review in soup.find_all('div', {'data-hook': 'review'}):
    review_text = review.find('span', {'data-hook': 'review-body'}).text.strip()
    reviews.append(review_text)

# Convert reviews to DataFrame
df = pd.DataFrame(reviews, columns=['Review'])

# Data Cleaning
stop_words = set(stopwords.words('english'))

def clean_review(review):
    review = review.replace('\n', ' ') # Remove newline characters
    review = review.replace('.', '') # Remove periods
    review = review.replace(',', '') # Remove commas
    review = review.replace('!', '') # Remove exclamation marks
    review = review.replace('?', '') # Remove question marks
    review = review.lower() # Convert to lowercase
    words = review.split() # Split review into words
    filtered_words = [word for word in words if word not in stop_words] # Remove stopwords
    return ' '.join(filtered_words) # Join words back into a single string

df['Cleaned_Review'] = df['Review'].apply(clean_review)

def get_sentiment(review):
    analysis = TextBlob(review)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

df['Sentiment'] = df['Cleaned_Review'].apply(get_sentiment)

# Data Visualization
plt.figure(figsize=(10, 6))
sns.countplot(x='Sentiment', data=df, palette='viridis')
plt.title('Sentiment Analysis of Amazon Customer Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.show()

df.head()
