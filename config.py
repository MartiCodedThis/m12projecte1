import os 

basedir = os.path.abspath(os.path.dirname(__file__))

# Config params
SECRET_KEY = "Valor aleatori molt llarg i super secret"
SQLALCHEMY_DATABASE_URI = "sqlite:///"
SQLALCHEMY_ECHO = True
