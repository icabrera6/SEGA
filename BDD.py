from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BibliotecaCapitan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

class Juego(db.Model):
    IdJuego = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50), nullable=True)
    Genero = db.Column(db.String(50), nullable=True)
    Descripcion = db.Column(db.String(200), nullable=True)
    Imagen = db.Column(db.String(50), nullable=True)

class Noticia(db.Model):
    IdNoticia = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String(50), nullable=True)
    Subtitulo = db.Column(db.String(50), nullable=True)
    Fecha = db.Column(db.Date, nullable=True)
    Contenido = db.Column(db.String(1000), nullable=True)
    Img = db.Column(db.String(200), nullable=True)

class Usuario(db.Model):
    IdUsuario = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50), nullable=True)
    Apellidos = db.Column(db.String(50), nullable=True)
    FechaNacimiento = db.Column(db.Date, nullable=True)
    Pais = db.Column(db.String(50), nullable=True)
    Email = db.Column(db.String(50), nullable=True)
    Contraseña = db.Column(db.String(50), nullable=True)
    EsAdmin = db.Column(db.Boolean, default=False)