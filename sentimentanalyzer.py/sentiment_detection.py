from textblob import TextBlob

def analyze_sentiment(text):
    # to make  an object of the TextBlob
    blob = TextBlob(text)
    # analyze the sentiment in the text (+ve, -ve, and neutral)
    sentiment = blob.sentiment
    polarity = round(sentiment.polarity, 3)
    subjectivity = round(sentiment.subjectivity, 3)

    
    if polarity > 0:
        sentiment_category = 'Positive'
    elif polarity < 0:
        sentiment_category = 'Negative'
    else:
        sentiment_category = 'Neutral'
    
    return sentiment_category, polarity, subjectivity


def main():
    text = input("Text: ")
    result = analyze_sentiment(text)
    print(f"Sentiment: {result}")
    

if __name__ == "__main__":
    main()
