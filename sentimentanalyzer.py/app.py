from flask import Flask, render_template, request
from sentiment_detection import analyze_sentiment
# render_template - to render html files
from textblob import TextBlob

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    polarity = None
    subjectivity = None
    
    if request.method == 'POST':
        text = request.form['text']
        sentiment, polarity, subjectivity = analyze_sentiment(text)
        
    return render_template('index.html', sentiment=sentiment, polarity=polarity, subjectivity=subjectivity)


if __name__ == "__main__":
    app.run(debug=True)
    