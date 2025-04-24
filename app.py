from flask import Flask, render_template, request
import re
import joblib

app = Flask(__name__)

# Load ML model and vectorizer
ml_model = joblib.load('ml_model.joblib')
vectorizer = joblib.load('vectorizer.joblib')

def is_real_email(email, content):
    # List of allowed domain extensions
    allowed_tlds = ['.com', '.io', '.net', '.in', '.org', '.gov.in']

    # Extract domain using regex
    match = re.search(r'@([\w\.-]+)', email)
    domain = match.group(1).lower() if match else None

    # Check for valid domain extension
    if domain:
        if not any(domain.endswith(tld) for tld in allowed_tlds):
            return "Fake", 0, "Invalid Domain Extension"

        # Extract company name from domain (e.g., google from google.com)
        domain_keyword = domain.split('.')[0]
        count = content.lower().count(domain_keyword)
        
        if count > 0:
            return "Real", count, "Domain Match"

    # Fallback to ML model if domain not matched or not found
    content_vec = vectorizer.transform([content])
    prediction = ml_model.predict(content_vec)[0]
    return prediction.capitalize(), 0, "ML Model"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        content = request.form['content']
        result, count, method = is_real_email(email, content)
        return render_template('index.html', result=result, count=count, method=method, email=email, content=content)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
