from flask import Flask, render_template, g, request, redirect, abort, url_for, flash
import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DATABASE CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
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
        db = g._database = sqlite3.connect('instance/database.db')
    return db

@app.route("/") 
def hello_world():
    return render_template('hello.html')

@app.route("/products/list") 
def list():
    with get_db() as con:
        products = con.execute('SELECT id, title, description, price FROM products ORDER BY id').fetchall()
    return render_template('products_list.html', products = products)

@app.route("/products/read/<int:id>") 
def read(id):
    with get_db() as con:
        products = con.execute('SELECT id, title, description, price FROM products WHERE id = ? ORDER BY id', (id,)).fetchall()
    return render_template('products_read.html', products = products)

@app.route("/products/update/<int:id>") 
def update(id):
    with get_db() as con:
        products = con.execute('SELECT id, title, description, price FROM products WHERE id = ? ORDER BY id', (id,)).fetchall()
    return render_template('products_update.html', products = products)

@app.route("/products/delete/<int:id>") 
def delete(id):
    with get_db() as con:
        products = con.execute('SELECT id, title, description, price FROM products WHERE id = ? ORDER BY id', (id,)).fetchall()
    return render_template('products_list.html', products = products)

@app.route("/products/create", methods=["GET","POST"]) 
def create():
    if request.method == "GET":
        return render_template("products_create.html")
    elif request.method == "POST":
        nom = request.form['nom']
        descripcio = request.form['descripcio']
        imatge = request.form['imatge']
        preu = request.form['preu']
        categoria = request.form['categoria']
    with get_db() as con:
        query = "INSERT INTO products (title, description, photo, price, category_id) VALUES (?, ?, ?, ?, ?)"
        con.execute(query, (nom,descripcio,imatge,preu,categoria))
        con.commit()
        return list()
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()