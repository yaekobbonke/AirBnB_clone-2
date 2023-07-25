#!/usr/bin/python3

"""
starts a Flask web application:
    the application is  listening on 0.0.0.0, port 5000
    uses storage for fetching data from the storage engine
    Routes:
    /states_list: display a HTML page

"""

from flask import Flask, render_template
from models import storage


@app.teardown_appcontext
def teardown_appcontext():
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """displays HTML page"""
    return render_template("7-states_list.html", state=state)



if __name__ == "__main__":
    app.run(host='0.0.0.0')
