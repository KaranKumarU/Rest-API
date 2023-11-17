import os

SECRET_KEY = os.urandom(32)

DEBUG = True

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:3306/northwind"

SQLALCHEMY_TRACK_MODIFICATIONS = False
