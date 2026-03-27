# 🚀 Flask + AWS Lambda Serverless Form Handler

A simple yet powerful serverless project demonstrating how a Flask application integrates with AWS Lambda via API Gateway to handle form submissions without managing backend servers.

---

## 🧠 Architecture Overview

User → Flask App → API Gateway → AWS Lambda → Response

---

## ⚙️ Tech Stack

- Python
- Flask
- AWS Lambda
- API Gateway

---

## 📌 Features

- Collect user input (Name & Email) via Flask form  
- Send data to serverless backend using API Gateway  
- Process request using AWS Lambda (Python)  
- Return JSON response back to Flask  

---

## 📷 Architecture Diagram

![Architecture](architecture.png)

---

## ▶️ How to Run Locally

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/flask-aws-lambda-serverless-form.git

# Navigate into project
cd flask-aws-lambda-serverless-form

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py
