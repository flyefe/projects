import os


class Config:
    SECRET_KEY = '1234'
    # Use SQLite for simplicity
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:maestro@localhost/maestro'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
