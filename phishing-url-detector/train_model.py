import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("dataset.csv")

X = data["url"]
y = data["label"]

vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vectorized, y)

joblib.dump(model, "model/phishing_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Model trained successfully!")