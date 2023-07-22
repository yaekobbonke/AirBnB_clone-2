#!/usr/bin/python3

"""
Flask application
listens on port 0.0.0.0
"""
from flask import Flask
n
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """ prints hello_HBNB """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
