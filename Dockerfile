FROM tiangolo/uwsgi-nginx-flask:python3.6

# Copy requirements.txt /
# python3.6 manage.py db upgrade && 
ADD . /watchlist-app

WORKDIR /watchlist-app

RUN pip install -r ./requirements.txt --no-cache-dir

ENV MOVIE_API_KEY=6809e9daeffd8c82b4ef74b653ae5ff7
ENV SECRET_KEY=iamasecretkey
CMD python3.6 manage.py runserver -h 0.0.0.0 -p 5000
