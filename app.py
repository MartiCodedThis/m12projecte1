from flask import Flask, render_template
import sqlite3
from flask import g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/") 
def hello_world():
    return render_template('hello.html')

@app.route('/list')
def list():
    return render_template("list.html")

# DATABASE CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Change this to your database URI
db = SQLAlchemy(app)

def init_db():
    with app.app_context():
        with app.open_resource('schema.sql', mode='r') as f:
            connection = db.engine.raw_connection()
            cursor = connection.cursor()
            cursor.executescript(f.read())
            connection.commit()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()