import pca2main
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('cleaned_titanic.csv')
# Encode categorical feature 'sex'
le = LabelEncoder()
df['sex_encoded'] = le.fit_transform(df['sex'])

X = df[['pclass', 'sex_encoded', 'age', 'fare']]
y = df['survived']

# 1. Decision Tree Classifier
dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X, y)
dt_preds = dt_classifier.predict(X)
print("Decision Tree Accuracy:", accuracy_score(y, dt_preds))

# 2. Gaussian Naive Bayes Classifier
gnb_classifier = GaussianNB()
gnb_classifier.fit(X, y)
gnb_preds = gnb_classifier.predict(X)
print("Gaussian Naive Bayes Accuracy:", accuracy_score(y, gnb_preds))

