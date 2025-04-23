# job-offer-classifier
# 📬 Job Offer Classifier

A Flask web application that classifies job offer emails as **Real** or **Fake** using email domain matching and a machine learning fallback model. This tool helps detect scam job offers by combining keyword analysis and company domain verification.

---

## 📌 Project Summary

This web app helps classify job offer emails as **Real** or **Fake** using two techniques:

1. **Email Domain Matching**: Extracts the domain from the sender’s email (e.g., `@amazon.com`) and checks its presence in the email content.
2. **Machine Learning Fallback**: If domain matching fails, the app uses a trained machine learning model to analyze email content and predict whether it’s genuine or suspicious.

---

## 📁 Project Structure

When you unzip or clone the project, you’ll find:


---

## ⚙️ Installation Steps

1. **Create a virtual environment** (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install flask scikit-learn joblib
python train_model.py
python app.py
Email:   careers@amazon.com  
Content: We are hiring at Amazon. Join us today.

---

### ✅ Steps to Push to GitHub:

1. Save this content as `README.md` in your project folder.
2. Open a terminal in that folder.
3. Run the following commands to push it to GitHub:

```bash
git init
git add .
git commit -m "Initial commit with Job Offer Classifier"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
