  
# Sentiment Detection Analyzer

Sentiment Detection Analyzer is a simple Flask-based web application that classifies user-entered text as **Positive**, **Negative**, or **Neutral**. It also provides detailed polarity and subjectivity scores, offering valuable insights into the tone and nature of the text. This tool is ideal for customer feedback analysis, social media trends, and general sentiment exploration.

---

## 🚀 Live Demo

Try the deployed application here: **[Sentiment Detection Analyzer](https://sentiment-analyzer-bo6z.onrender.com/)**

---

## Features

- **Sentiment Classification**: Categorizes text as Positive, Negative, or Neutral.
- **Polarity & Subjectivity Scores**: Understand the strength and tone of sentiment.
- **User-Friendly Interface**: Clean, intuitive web interface for seamless interaction.

---

## Installation

To run the project locally, follow these steps:

### Prerequisites
- **Python 3.7+** installed
- **Git** installed

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/sentiment-detection-analyzer.git
   cd sentiment-detection-analyzer
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and visit:
   ```
   http://127.0.0.1:5000
   ```

---

## Deployment on Render

The app is deployed on Render at **[https://sentiment-analyzer-bo6z.onrender.com/](https://sentiment-analyzer-bo6z.onrender.com/)**.

### Steps to Deploy on Render
1. Push your project to a GitHub repository.
2. Log in to [Render](https://render.com/) and create a **new web service**.
3. Connect your GitHub repository.
4. Use the following settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Save and deploy!

---

## Project Structure

```
sentiment-detection-analyzer/
│
├── app.py                 # Main Flask application
├── sentiment_detection.py # Sentiment analysis logic using TextBlob
├── requirements.txt       # Python dependencies
├── Procfile               # Configuration for deployment
├── runtime.txt            # Python runtime version
│
├── static/                # Static assets like CSS
│   └── css/
│       └── styles.css     # Styling for the app
│
├── templates/             # HTML templates
│   └── index.html         # Main webpage
│
└── __pycache__/           # Compiled Python files
```

---

## Technologies Used

- **Flask**: Lightweight Python web framework.
- **TextBlob**: NLP library for sentiment analysis.
- **Gunicorn**: WSGI HTTP server for running Python applications.
- **HTML/CSS**: Frontend design.

---

## Contributing

Contributions are welcome! If you have ideas for improvements or new features:
1. Fork this repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m 'Add a feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a Pull Request.

---

## Author

Developed by **Mohammed Faiz**  
Contact: [mohammedfaiz506@gmail.com](mailto:mohammedfaiz506@gmail.com) | [GitHub Profile](https://github.com/Faizme)
