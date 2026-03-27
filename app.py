from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_URL = "YOUR_API_GATEWAY_URL"

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "name": request.form['name'],
        "email": request.form['email']
    }

    try:
        response = requests.post(API_URL, json=data)
        result = response.json()

        return f"""
        <h3>Response from Lambda:</h3>
        <p>{result}</p>
        <a href="/">Go Back</a>
        """

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    