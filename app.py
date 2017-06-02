from flask import Flask, render_template, request
import webbrowser
import os, requests, json, ssl

app = Flask(__name__, static_url_path='')

@app.route('/')
#@requires_auth
def home():
    return "YOLO"

@app.route('/open/<path:url>')
def openDefaultWebBrowser(url):
    webbrowser.open(url)
    return url


if __name__ == "__main__":
    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8000)))
