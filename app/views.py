from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    view root page function that returns index and it\'s data
    '''
    return render_template('index.html')