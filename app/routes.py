from app import app
from flask import render_template, redirect, url_for

#home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/games')
def games():
    return render_template('games.html')