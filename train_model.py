import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample training dataset
X_train = [
    "Congratulations! You've won a free prize. Click here to claim.",
    "This is a job offer from Microsoft company.",
    "Urgent: Your account will be locked. Verify now.",
    "We are hiring at Google. Join us now.",
    "Free money just for signing up!",
    "Dear user, we are happy to offer you a position at Apple.",
    "Job opportunity at Amazon. Apply now.",
    "Limited time job offer! Act fast.",
    "We are a trusted recruiter from Facebook.",
    "Click to win a new job offer instantly."
]

y_train = ['fake', 'real', 'fake', 'real', 'fake', 'real', 'real', 'fake', 'real', 'fake']

# Use TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Save model and vectorizer
joblib.dump(model, 'ml_model.joblib')
joblib.dump(vectorizer, 'vectorizer.joblib')
