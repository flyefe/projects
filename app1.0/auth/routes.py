from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.models import User  # Import the User model from app/models
from app import db


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    # Add your signup view here
    pass


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Add your login view here
    pass


@auth.route('/logout')
@login_required
def logout():
    # Add your logout view here
    pass
