import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

# Load the dataset
data = pd.read_csv('study_plan_dataset.csv')  # Ensure your CSV path is correct

# Data Preprocessing
X = data['prompt']  # Input feature
y = data['completion']  # Target variable

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Extraction
vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, ngram_range=(1, 2))
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Model Training
model = LogisticRegression(class_weight='balanced')
model.fit(X_train_tfidf, y_train)

# Evaluation
y_pred = model.predict(X_test_tfidf)
print(classification_report(y_test, y_pred))

# Save the model and vectorizer
joblib.dump(model, 'study_plan_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
