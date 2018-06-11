from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    view root page function that returns index and it\'s data
    '''
    title = 'Home - Welcome to the best movie review website online'
    return render_template('index.html', title = title)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    view movie page function that returns movies and all it\'s data
    '''
    title = 'Home - Welcome to the best movie review website online'
    return render_template('movie.html', id = movie_id)
