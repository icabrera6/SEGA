from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BibliotecaCapitan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class Juego(db.Model):
    Id=db.Column(db.Integer, primary_key=True)
    Nombre=db.Column(db.String(50), nullable=True)
    Genero=db.Column(db.String(50), nullable=True)
    Descripcion=db.Column(db.String(50), nullable=True)
    Imagen=db.Column(db.String(50), nullable=True)

@app.route('/añadir_juego',methods=["GET","POST"])
def add_game():
    if request.method == 'POST':
        id = request.form.get('id')
        fecha_nacimiento = request.form.get('fecha_nacimiento')
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')            
        pais = request.form.get('pais')
        gmail = request.form.get('gmail')
        nuevo_usuario = Juego(Id=id, Fecha_nacimiento=fecha_nacimiento, Nombre=nombre, Apellidos=apellidos, Pais=pais, Gmail=gmail)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return redirect(url_for('get_libros'))