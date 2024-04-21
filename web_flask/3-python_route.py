#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask
app = Flask(__name__)

# Route for the root URL
@app.route('/', strict_slashes=False)
def index():
    """Returns a greeting message."""
    return 'Hello HBNB!'

# Route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a message indicating HBNB."""
    return 'HBNB'

# Route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Returns "C " followed by the value of the text variable."""
    return 'C ' + text.replace('_', ' ')

# Route for '/python' and '/python/<text>'
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """Returns "Python ", followed by the value of the text variable."""
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

