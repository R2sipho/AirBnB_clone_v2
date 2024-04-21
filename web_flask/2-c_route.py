#!/usr/bin/python3
""" Starts a Flask Web Application - C is FUN """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns a greeting message when the root route is accessed """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns a message indicating HBNB when the /hbnb route is accessed """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Returns a message indicating the provided text is fun with C """
    return "C " + text.replace('_', ' ')

if __name__ == "__main__":
    """ Main function to run the Flask application """
    app.run(host='0.0.0.0', port=5000)

