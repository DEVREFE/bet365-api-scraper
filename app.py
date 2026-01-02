from flask import Flask, render_template
from inplaydiaryapi import InPlays
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    try:
        in_plays = InPlays()
        matches = in_plays.on()
    except Exception as e:
        app.logger.error(f"Error fetching matches: {e}")
        matches = []

    return render_template('index.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
