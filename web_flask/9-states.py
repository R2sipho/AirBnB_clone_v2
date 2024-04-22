#!/usr/bin/python3
"""Module: Starts a Flask web app and fetches data from storage engine"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def close_session(exception):
    """Closes the current SQLAlchemy session"""
    storage.close()

@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_state(id=None):
    """Lists states from the storage engine"""
    states = None
    state = None

    if id:
        states = storage.all(State)
        key = 'State.' + id
        state = states.get(key)

    else:
        states = storage.all(State).values()

    return render_template('9-states.html', states=states, state=state)

if __name__ == '__main__':
    storage.reload()
    app.run(host="0.0.0.0", port="5000")

