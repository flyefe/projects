from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app import app, db
from app.models import User


@app.route('/')
def index():
    # return render_template('index.html')
    return 'Welcome to home page'

# Add more routes and views as needed for your app's functionality
