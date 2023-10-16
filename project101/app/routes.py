from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user, user_login_confirmed
from app import app, db
from app.models import User


@app.route('/')
def index():
    # @login_required
    # return render_template('index.html', user=user)
    # return render_template('index.html')
    return 'Welcome to home page'

# Add more routes and views as needed for your app's functionality
