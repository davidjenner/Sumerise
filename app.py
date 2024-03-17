from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the summarization pipeline
summarizer = pipeline("summarization")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.form['text']
    summary = summarizer(data, max_length=130, min_length=30, do_sample=False)
    return jsonify(summary[0]['summary_text'])

if __name__ == '__main__':
    app.run(debug=True)
