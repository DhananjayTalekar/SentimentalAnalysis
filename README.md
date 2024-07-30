
# Sentiment Analysis of Amazon Customer Reviews

## Overview

This project performs sentiment analysis on customer reviews from Amazon. It involves web scraping to gather review data, cleaning the data to remove unwanted characters and stopwords, conducting sentiment analysis to classify the reviews as positive, neutral, or negative, and visualizing the sentiment distribution.

## Skills Required

- **Python Programming**: Essential for writing scripts and automating tasks.
- **Web Scraping**: Using `requests` and `BeautifulSoup` libraries to extract data from websites.
- **Data Cleaning**: Utilizing `pandas` for handling and preprocessing datasets.
- **Text Processing**: Employing `nltk` for tokenization and stopword removal.
- **Sentiment Analysis**: Applying `TextBlob` for basic sentiment analysis.
- **Data Visualization**: Creating visual representations of data using `matplotlib` and `seaborn`.
- **VS Code**: Proficiency in using VS Code for developing and running the project.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/DhananjayTalekar/SentimentalAnalysis
   cd SentimentalAnalysis
   ```

2. **Install Required Libraries**:
   Open a terminal and run the following command:
   ```sh
   pip install requests beautifulsoup4 pandas nltk textblob matplotlib seaborn
   ```

3. **Download NLTK stopwords**:
   ```sh
   python -c "import nltk; nltk.download('stopwords')"
   ```

## Usage

1. **Run the Script**:
   Execute the script by running the following command in the terminal:
   ```sh
   python sentiment_analysis.py
   ```

2. **Expected Output**:
   - The script will scrape customer reviews from the provided Amazon link.
   - It will clean the data using simpler methods.
   - Perform sentiment analysis on the reviews.
   - Display a plot showing the sentiment distribution of the reviews.
   - Print the first few rows of the DataFrame with original and cleaned reviews and their sentiments.

## Example Output

### DataFrame Head
```
                                             Review                                      Cleaned_Review Sentiment
0  Great product! Works as expected. Very satisfied.  great product works expected satisfied       Positive
1                    Not worth the price. Disappointed.                      not worth price disappointed       Negative
2  Just okay. Nothing special.                            just okay nothing special       Neutral
```

### Sentiment Distribution Plot
![Sentiment Analysis Plot]![Sentiment image](https://github.com/user-attachments/assets/e97f8de6-5060-4df9-9e8d-10502179826b)



