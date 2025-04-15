from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BibliotecaCapitan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)

class Usuario(db.Model):
    IdUsuario = db.Column(db.Integer, primary_key=True)
    Fecha_nacimiento = db.Column(db.Date, nullable=True)
    Nombre = db.Column(db.String(50), nullable=True)
    Apellidos = db.Column(db.String(50), nullable=True)
    Pais = db.Column(db.String(50), nullable=True)
    Gmail = db.Column(db.String(50), nullable=True)
    EsAdmin = db.Column(db.Boolean, nullable=False)

#Añadir un usuario (registrarse)
@app.route('/registro', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        id = request.form.get('idusuario')
        fecha_nacimiento = request.form.get('fecha_nacimiento')
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')            
        pais = request.form.get('pais')
        gmail = request.form.get('gmail')
        esAdmin = False
        nuevo_usuario = Usuario(IdUsuario=id, Fecha_nacimiento=fecha_nacimiento, Nombre=nombre, Apellidos=apellidos, Pais=pais, Gmail=gmail, EsAdmin=esAdmin)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return redirect(url_for('get_libros'))
        
        #return render_template('new_libro.html')

if __name__ == '__main__':
    app.run(debug=True)