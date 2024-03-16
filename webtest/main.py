# Import
from flask import Flask, render_template, redirect, url_for

# Define constants
APP = Flask(__name__)

# Routes
@APP.route('/')
def home():
    return redirect(url_for('example'))

@APP.route('/example')
def example():
    return render_template('example.html')

if __name__ == '__main__':
    APP.run(debug=True)