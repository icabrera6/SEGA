from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BibliotecaCapitan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class Noticia(db.Model):
    IdNoticia=db.Column(db.Integer, primary_key=True)
    Titulo=db.Column(db.String(50), nullable=True)
    Subtitulo=db.Column(db.String(50), nullable=True)
    Fecha=db.Column(db.Date, nullable=True)
    Contenido=db.Column(db.String(300), nullable=True)
    Imagen=db.Column(db.String(50), nullable=True)

@app.route('/añadir_noticia',methods=["GET","POST"])
def add_game():
    if request.method == 'POST':
        id = request.form.get('idnoticia')
        titulo = request.form.get('titulo')
        subtitulo = request.form.get('subtitulo')
        fecha = request.form.get('fecha')
        contenido = request.form.get('contenido')
        imagen = request.form.get('imagen')
        nueva_noticia = Noticia(IdNoticia=id, Titulo=titulo, Subtitulo=subtitulo, Fecha=fecha, Contenido=contenido, Imagen=imagen)
        db.session.add(nueva_noticia)
        db.session.commit()
        return redirect(url_for('get_libros'))

if __name__ == '__main__':
    app.run(debug=True)