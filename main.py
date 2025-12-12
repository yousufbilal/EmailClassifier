import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix


df = pd.read_csv('email_dataset.csv')
df["clean_text"]=(
    df["text"]
   .str.lower()
    .str.replace("\n", " ", regex=False)
    .str.replace("\r", " ", regex=False)
    .str.strip()
)

texts= df["clean_text"]
label= df["label"]

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(texts)

X_train, X_test, y_train, y_test = train_test_split(
    X, label, test_size=0.2, random_state=42
)

##train 
model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
# print("Predictions:", list(y_pred))
# print("Actual:", list(y_test))






