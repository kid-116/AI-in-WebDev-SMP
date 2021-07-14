import flask
from flask import Flask, render_template
import recsys
import numpy as np
import data

app = Flask(__name__)

@app.route('/', methods=['GET'])
def landing():
    return render_template('landing.html')

@app.route('/preferences', methods=['GET', 'POST'])
def get_prefs():
    movies = data.data['name']
    if flask.request.method == 'POST':
        movie_count = len(movies)
        input_ratings = np.zeros(movie_count)
        for i in range(movie_count):
            input_ratings[i] = flask.request.values.get(movies[i])
        return process_recs(input_ratings)
    return render_template('prefs.html', movies=movies)

@app.route('/recommendations', methods=['GET'])
def process_recs(input_ratings):
    recs = recsys.predict(input_ratings)
    return render_template('recs.html', recs=recs)

if __name__ == '__main__':
    app.run()