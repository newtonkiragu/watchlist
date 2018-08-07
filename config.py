import os

class  Config:
    '''
    General configuration parent class
    '''

    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = '6809e9daeffd8c82b4ef74b653ae5ff7'
    SECRET_KEY = 'iamasecretkey'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://monster:manager666@localhost/watchlist'

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config : The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
