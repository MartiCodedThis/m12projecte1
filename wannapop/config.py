import os 
from os import environ, path

basedir = os.path.abspath(os.path.dirname(__file__))

# Config params
SECRET_KEY = "Valor aleatori molt llarg i super secret"
SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir, "../database.db")
SQLALCHEMY_ECHO = False 

MAIL_SENDER_NAME = environ.get('MAIL_SENDER_NAME')
MAIL_SENDER_ADDR = environ.get('MAIL_SENDER_ADDR')
MAIL_SENDER_PASSWORD = environ.get('MAIL_SENDER_PASSWORD')
MAIL_SMTP_SERVER = environ.get('MAIL_SMTP_SERVER')
MAIL_SMTP_PORT = int(environ.get('MAIL_SMTP_PORT'))

CONTACT_ADDR = environ.get('CONTACT_ADDR')

EXTERNAL_URL = environ.get('EXTERNAL_URL')

DEBUG = environ.get('DEBUG', False)