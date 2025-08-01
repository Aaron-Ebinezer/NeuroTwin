import joblib
from sklearn.metrics import classification_report

# Load saved model
clf = joblib.load("models/mm_iq_clf.joblib")
vectorizer = joblib.load("models/tfidf.joblib")

# Test on held-out data
X_test_vec = vectorizer.transform(X_test)
print(classification_report(y_test, clf.predict(X_test_vec)))