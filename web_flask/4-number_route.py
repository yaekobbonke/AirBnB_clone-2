#!/usr/bin/python3

"""
starts a Flask web application:
    listening on 0.0.0.0, port 5000
Routes:
    /: displays "Hello HBNB!"
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable
    replace underscore _ symbols with a space
    /python/(<text>): display “Python ”, followed by the value of the
    text variable replace underscore _ symbols with a space
    The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """displays Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<n>", strict_slashes=False)
def n_number(n):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
