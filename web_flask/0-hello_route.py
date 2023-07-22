#!/usr/bin/python3
# Flask module
from flask import Flask
# Flask class initialization
app = Flask(__name__)
@app.route("/", strict_slashes=False)
# Flask view function
def hello_HBNB():
    print('HELLO HBNB')

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
