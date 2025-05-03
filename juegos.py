from flask import Blueprint, Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from BDD import db, Juego

BPjuegos = Blueprint('BPjuegos', __name__)

@BPjuegos.route('/añadir_juego', methods=["GET", "POST"])
def add_game():
    if request.method == 'POST':
        nombre = request.form.get('Nombre')
        genero = request.form.get('Genero')
        descripcion = request.form.get('Descripcion')
        imagen = request.form.get('Imagen')
        nuevo_juego = Juego(Nombre=nombre, Genero=genero, Descripcion=descripcion, Imagen=imagen)
        db.session.add(nuevo_juego)
        db.session.commit()
        return redirect(url_for('add_game'))
    return render_template('add.html')

@BPjuegos.route('/juegos')
def juegos():
    todos = Juego.query.all()
    return render_template('juegos/juegos.html', juegos=todos)