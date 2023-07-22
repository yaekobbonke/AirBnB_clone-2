#!/usr/bin/python3
"""
starts flask application
listens on 0.0.0.0
It has two routes
"/" returns HELLO HBNB
"/hbnb" returns HBNB
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays HELLO HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb",strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


if __name__ == "__main__.py":
    app.run(host='0.0.0.0', port = 5000)
