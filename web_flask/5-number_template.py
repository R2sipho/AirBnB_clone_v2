#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template
app = Flask(__name__)

# Route for the root URL
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a greeting message."""
    return 'Hello HBNB!'

# Route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Returns a message indicating HBNB."""
    return 'HBNB'

# Route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Returns "C ", followed by the value of the text variable."""
    return 'C ' + text.replace('_', ' ')

# Route for '/python' and '/python/<text>'
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """Returns "Python ", followed by the value of the text variable."""
    return 'Python ' + text.replace('_', ' ')

# Route for '/number/<n>'
@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Returns "n is a number" only if n is an integer."""
    return '{} is a number'.format(n)

# Route for '/number_template/<n>'
@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Returns an HTML page with 'Number: n' if n is an integer."""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

