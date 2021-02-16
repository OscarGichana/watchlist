from flask import render_template
from app import app



@app.route('/movie/<movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie_id = 1234
    return render_template('movie.html',id = movie_id)

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    movie_id = 1234
    message = 'Hello World Im new'
    return render_template('index.html',message = message, id = movie_id)



