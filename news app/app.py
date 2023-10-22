from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '934fbfdfdcdd4af2937f0215323e5df2'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = request.form['category']
        date_filter = request.form['date_filter']
        q = request.form['q']
        url = 'https://newsapi.org/v2/top-headlines'
        params = {
            'apiKey': API_KEY,
            'country': 'TR',  # Default country, you can change it as per your requirement
            'category': category,
            'q': q
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            articles = data['articles']
            return render_template('news.html', articles=articles)
        else:
            return "Error occurred: " + response.text
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)