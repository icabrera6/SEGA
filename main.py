from flask import Blueprint, Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from BDD import db, Juego, Noticia, Usuario
from noticias import BPnoticias
from usuarios import BPusuarios
from juegos import BPjuegos
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BibliotecaCapitan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(BPnoticias, url_prefix='/noticias')
app.register_blueprint(BPusuarios, url_prefix='/usuarios')
app.register_blueprint(BPjuegos, url_prefix='/juegos')

@app.route('/',methods=["GET","POST"])
def cargar_login():
    return render_template('usuarios/login.html')
@app.route('/index',methods=["GET","POST"])
def cargar_index():
    return render_template('index.html')
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)