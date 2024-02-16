import os 
from os import environ, path

basedir = os.path.abspath(os.path.dirname(__file__))



# Config params
LOG_LEVEL = environ.get('LOG_LEVEL', 'DEBUG').upper()

SECRET_KEY = "Valor aleatori molt llarg i super secret"
# SQLite #
# SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir, "../database.db")

# MySQL #
# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://2dd06:uttVEcUemINNCX47@37.27.3.70:3306/2dd06_my"
# MySQL Docker#
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:HOWDOYOUTURNTHISON@127.0.0.1:3306/userdb"

# PostgreSQL #
#SQLALCHEMY_DATABASE_URI = "postgresql://2dd06:uttVEcUemINNCX47@37.27.3.70:5432/2dd06_pg"

SQLALCHEMY_ECHO = False 

MAIL_SENDER_NAME = environ.get('MAIL_SENDER_NAME')
MAIL_SENDER_ADDR = environ.get('MAIL_SENDER_ADDR')
MAIL_SENDER_PASSWORD = environ.get('MAIL_SENDER_PASSWORD')
MAIL_SMTP_SERVER = environ.get('MAIL_SMTP_SERVER')
MAIL_SMTP_PORT = int(environ.get('MAIL_SMTP_PORT'))

CONTACT_ADDR = environ.get('CONTACT_ADDR')

EXTERNAL_URL = environ.get('EXTERNAL_URL')

DEBUG = environ.get('DEBUG', False)

DEBUG_TB_INTERCEPT_REDIRECTS = False