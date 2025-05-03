from flask import Blueprint, Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from BDD import db, Usuario

BPusuarios = Blueprint('BPusuarios', __name__)

@BPusuarios.route('/signup', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        nombre = request.form.get('Nombre')
        apellidos = request.form.get('Apellidos')
        fechanacimiento = request.form.get('FechaNacimiento')
        fechanacimientomod = datetime.strptime(fechanacimiento, '%Y-%m-%d').date()
        pais = request.form.get('Pais')
        email = request.form.get('Email')
        contraseña = request.form.get('Contraseña')
        nuevo_usuario = Usuario(Nombre=nombre, Apellidos=apellidos, FechaNacimiento=fechanacimientomod, Pais=pais, Email=email, Contraseña=contraseña)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return redirect(url_for('BPusuarios.login_user'))
    return render_template('usuarios/signup.html')

@BPusuarios.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == "POST":
        email = request.form.get('Email')
        usuario = Usuario.query.filter_by(Email=email).first()
        contraseña = request.form.get('Contraseña')
        if usuario and contraseña == usuario.Contraseña:
            return render_template('index.html')
        else:
            return render_template('usuarios/login.html')
    return render_template('usuarios/login.html')

# Perfil de usuario
@BPusuarios.route('/user/<int:user_id>')
def user_profile(user_id):
    user = Usuario.query.get(user_id)
    if user:
        return render_template('user_profile.html', user=user)
    else:
        return render_template('user_profile_failed.html')