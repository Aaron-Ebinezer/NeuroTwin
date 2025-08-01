import joblib

# Load artifacts
clf = joblib.load("models/mm_iq_clf.joblib")
vectorizer = joblib.load("models/tfidf.joblib")

# Interactive demo
while True:
    user_input = input("Enter a question (or 'quit'): ")
    if user_input.lower() == "quit":
        break
    vec = vectorizer.transform([user_input])
    print(f"Predicted difficulty: {clf.predict(vec)[0]}")