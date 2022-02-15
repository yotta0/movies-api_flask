import requests
from flask import Blueprint, render_template, request, current_app

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/movies')
def get_movies():
    url = f'https://api.themoviedb.org/3/movie/550?api_key={current_app.config["API_KEY"]}'
    req = requests.get(url)
    return req.json()