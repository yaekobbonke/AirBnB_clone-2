#!/usr/bin/python3

"""
starts Flask application
listens on 127.0.0.1, port 5000
route:
    "/airbnb-onepage/"
"""
from flask import Flask
app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_HBNB():
    """ Displays HELLO HBNB """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
