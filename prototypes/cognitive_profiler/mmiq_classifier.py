from datasets import load_dataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib 

dataset = load_dataset("huanqia/MM-IQ", split="train")
df = pd.DataFrame(dataset)

texts = df["question"].tolist()
difficulty = df["difficulty"].tolist()  

X_train, X_test, y_train, y_test = train_test_split(
    texts, difficulty, test_size=0.2, random_state=42
)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=1000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

clf = RandomForestClassifier(n_estimators=50)
clf.fit(X_train_vec, y_train)

joblib.dump(clf, "prototypes/cognitive_profiler/models/mm_iq_clf.joblib")
joblib.dump(vectorizer, "prototypes/cognitive_profiler/models/tfidf.joblib")

test_pred = clf.predict(X_test_vec)
print(pd.crosstab(y_test, test_pred, rownames=["Actual"], colnames=["Predicted"]))