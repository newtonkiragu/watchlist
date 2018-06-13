from flask import render_template
from app import app
from .request import get_movies

#views
@app.route('/')
def index():
    '''
    view root page function that returns index and it\'s data
    '''

    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to the best movie review website online'
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    view movie page function that returns movies and all it\'s data
    '''
    title = 'Movie - Welcome to the best movie review website online'
    return render_template('index.html', title = title,popular = popular_movies)
