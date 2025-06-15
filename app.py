
    
from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route("/", methods=["GET", "POST"])
def home():
    summary = None
    if request.method == "POST":
        text = request.form.get("text", "")
        if text.strip():
            result = summarizer(text, max_length=100, min_length=30, do_sample=False)
            summary = result[0]['summary_text']
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)  