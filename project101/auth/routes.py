from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.models import User  # Import the User model from app/models
from app import db


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists', 'error')
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(
                password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully', 'success')
            login_user(new_user)
            return redirect(url_for('appindex'))

    return render_template('signup.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Add your login view here
    pass


@auth.route('/logout')
@login_required
def logout():
    # Add your logout view here
    pass
