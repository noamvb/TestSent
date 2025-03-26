from flask import Flask, render_template, request, jsonify
from sentiment_analyzer import SentimentAnalyzer

app = Flask(__name__)
analyzer = SentimentAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Get text from request
    text = request.form.get('text', '')
    
    # Analyze the sentiment
    if text:
        result = analyzer.analyze(text)
        result['emoji'] = analyzer.get_emoji(result['sentiment'])
        return jsonify(result)
    else:
        return jsonify({"error": "No text provided"})

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    # API endpoint that accepts JSON
    data = request.get_json()
    text = data.get('text', '') if data else ''
    
    # Analyze the sentiment
    if text:
        result = analyzer.analyze(text)
        result['emoji'] = analyzer.get_emoji(result['sentiment'])
        return jsonify(result)
    else:
        return jsonify({"error": "No text provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)