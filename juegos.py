from flask import Blueprint, Flask, render_template, request, redirect, url_for, session, current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from BDD import db, Juego
import os
from werkzeug.utils import secure_filename
BPjuegos = Blueprint('BPjuegos', __name__)

@BPjuegos.route('/añadir_juego', methods=["GET", "POST"])
def add_game():
    if request.method == 'POST':
        nombre = request.form.get('Nombre')
        genero = request.form.get('Genero')
        descripcion = request.form.get('Descripcion')
        imagen = request.files['Img']
        nombreimagen = secure_filename(imagen.filename)
        ruta = os.path.join(current_app.config['UPLOAD_FOLDER'], nombreimagen)
        imagen.save(ruta)
        rutaimagen = '../../static/img/'+nombreimagen
        nuevo_juego = Juego(Nombre=nombre, Genero=genero, Descripcion=descripcion, Imagen=rutaimagen)
        db.session.add(nuevo_juego)
        db.session.commit()
        return redirect(url_for('BPjuegos.add_game'))
    es_admin = session.get('admin', False)
    return render_template('juegos/gestionar_juegos.html', es_admin=es_admin)

@BPjuegos.route('/juegos')
def juegos():
    juegos = Juego.query.all()
    es_admin = session.get('admin', False)
    return render_template('juegos/juegos.html', juegos=juegos, es_admin=es_admin)

@BPjuegos.route('/gestion_juegos')
def gestion_juegos():
    es_admin = session.get('admin', False)
    return render_template('juegos/gestionar_juegos.html', es_admin=es_admin)

@BPjuegos.route('/detalle_juego', methods=['POST'])
def delete_game(juego_id):
    juego = Juego.query.get(juego_id)
    print(juego)