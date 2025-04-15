from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BibliotecaCapitan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class Juego(db.Model):
    IdJuego=db.Column(db.Integer, primary_key=True)
    Nombre=db.Column(db.String(50), nullable=True)
    Genero=db.Column(db.String(50), nullable=True)
    Descripcion=db.Column(db.String(50), nullable=True)
    Imagen=db.Column(db.String(50), nullable=True)

@app.route('/añadir_juego',methods=["GET","POST"])
def add_game():
    if request.method == 'POST':
        id = request.form.get('idjuego')
        nombre = request.form.get('nombre')
        genero = request.form.get('genero')
        descripcion = request.form.get('descripcion')
        imagen = request.form.get('imagen')
        nuevo_juego = Juego(IdJuego=id, Nombre=nombre, Genero=genero, Descripcion=descripcion, Imagen=imagen)
        db.session.add(nuevo_juego)
        db.session.commit()
        return redirect(url_for('get_libros'))

if __name__ == '__main__':
    app.run(debug=True)