from flask import Flask, render_template, request
from datetime import datetime
import joblib

app = Flask(__name__)

model = joblib.load("model/phishing_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

history = []

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    confidence = ""

    if request.method == "POST":

        url = request.form["url"]

        url_vector = vectorizer.transform([url])

        prediction = model.predict(url_vector)

        probability = model.predict_proba(url_vector)
        confidence = round(max(probability[0]) * 100, 2)

        if prediction[0] == 1:
            result = "⚠️ Phishing URL Detected!"
        else:
            result = "✅ Safe URL"

        history.insert(0, {
            "url": url,
            "result": result,
            "confidence": confidence,
            "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

    total_scans = len(history)

    safe_count = sum(
        1 for item in history
        if "Safe" in item["result"]
    )

    phishing_count = sum(
        1 for item in history
        if "Phishing" in item["result"]
    )

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        history=history,
        total_scans=total_scans,
        safe_count=safe_count,
        phishing_count=phishing_count
    )

@app.route("/clear")
def clear():

    history.clear()

    return render_template(
        "index.html",
        history=[],
        result="",
        confidence="",
        total_scans=0,
        safe_count=0,
        phishing_count=0
    )

if __name__ == "__main__":
    app.run(debug=True)