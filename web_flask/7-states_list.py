#!/usr/bin/python3
"""Script that list all states"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """displays a new HTML page"""
    new_dict = storage.all('State')
    return render_template('7-states_list.html', states=new_dict)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
