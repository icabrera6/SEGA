from flask import Blueprint, Flask, jsonify, render_template, request, redirect, url_for, session, current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from BDD import db, Noticia
import os
from werkzeug.utils import secure_filename

BPnoticias = Blueprint('BPnoticias', __name__)

@BPnoticias.route('/añadir_noticia', methods=['GET', 'POST'])
def add_noticia():
    if request.method == 'POST':
        titulo = request.form.get('Titulo')
        subtitulo = request.form.get('Subtitulo')            
        fecha = request.form.get('Fecha')
        fechamod = datetime.strptime(fecha, '%Y-%m-%d').date()
        contenido = request.form.get('Contenido')
        img = request.files['Img']
        nombre = secure_filename(img.filename)
        print(f"Titulo: {titulo}, Subtitulo: {subtitulo}, Fecha: {fecha}, Contenido: {contenido}, Img: {nombre}")
        ruta = os.path.join(current_app.config['UPLOAD_FOLDER'], nombre)
        img.save(ruta)
        rutaimg = '../../static/img/'+nombre
        nueva_noticia = Noticia(Titulo=titulo, Subtitulo=subtitulo, Fecha=fechamod, Contenido=contenido, Img=rutaimg)
        db.session.add(nueva_noticia)
        db.session.commit()
        return redirect(url_for('BPnoticias.add_noticia'))
    es_admin = session.get('admin', False)
    return render_template('noticias/gestionar_noticias.html', es_admin=es_admin)  

@BPnoticias.route('/noticias')
def noticias():
    todas = Noticia.query.all()
    es_admin = session.get('admin', False)
    return render_template('noticias/noticias.html', noticias=todas, es_admin=es_admin)

# Eliminar noticia
@BPnoticias.route('/noticia/delete/<int:noticia_id>', methods=['POST'])
def delete_noticia(noticia_id):
    noticia = Noticia.query.get(noticia_id)
    if noticia:
        db.session.delete(noticia)
        db.session.commit()
        return f"Mensaje: La noticia con el ID {noticia_id} ha sido eliminada correctamente."
    else:
        return jsonify({"error": "Noticia no encontrada"}), 404

# Editar noticia
@BPnoticias.route('/noticia/edit/<int:noticia_id>', methods=['GET', 'POST'])
def edit_noticia(noticia_id):
    noticia = Noticia.query.get_or_404(noticia_id)
    if request.method == 'POST':
        noticia.Juego = request.form.get('juego')
        noticia.Titulo = request.form.get('titulo')
        noticia.Texto = request.form.get('texto')
        noticia.Img = request.form.get('img')
        db.session.commit()
        return redirect(url_for('noticias')) 
    return render_template('edit_libro.html', noticia=noticia)

@BPnoticias.route('/gestion_noticias')
def gestion_noticias():
    es_admin = session.get('admin', False)
    return render_template('noticias/gestionar_noticias.html',es_admin=es_admin)