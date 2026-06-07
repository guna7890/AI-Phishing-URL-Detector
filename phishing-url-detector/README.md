# AI Phishing URL Detector

## Project Overview

AI Phishing URL Detector is a cybersecurity project that uses Machine Learning to identify whether a URL is safe or phishing.

The application is built using Python, Flask, Scikit-Learn, HTML, and CSS.

---

## Features

- Detects phishing URLs
- Detects safe URLs
- Confidence score prediction
- Detection history
- Statistics dashboard
- User-friendly web interface

---

## Technologies Used

- Python
- Flask
- Machine Learning
- Scikit-Learn
- TF-IDF Vectorizer
- Logistic Regression
- HTML
- CSS

---

## Project Structure

```text
phishing-url-detector/
│
├── app.py
├── train_model.py
├── dataset.csv
├── requirements.txt
│
├── model/
│   ├── phishing_model.pkl
│   └── vectorizer.pkl
│
└── templates/
    └── index.html
```

---

## How To Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Machine Learning Model

- TF-IDF Vectorizer
- Logistic Regression

The model is trained using a dataset containing safe and phishing URLs.

---

## Author

Guna Shekar Reddy

Cybersecurity & Artificial Intelligence Project