from flask import Blueprint, Flask, jsonify, render_template, request, redirect, url_for, session
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
        esadmin = request.form.get('EsAdmin') == 'on'
        nuevo_usuario = Usuario(Nombre=nombre, Apellidos=apellidos, FechaNacimiento=fechanacimientomod, Pais=pais, Email=email, Contraseña=contraseña, EsAdmin=esadmin)
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
            session['admin'] = True if usuario.EsAdmin else False
            return render_template('index.html', es_admin=session['admin'])
        else:
            return render_template('usuarios/login.html')
    return render_template('usuarios/login.html')

@BPusuarios.route('/cerrar_sesion', methods=['GET', 'POST'])
def log_out():
    session.pop('admin', None)
    return render_template('usuarios/login.html')

@BPusuarios.route('/registrar_usuario', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        nombre = request.form.get('Nombre')
        apellidos = request.form.get('Apellidos')
        fechanacimiento = request.form.get('FechaNacimiento')
        fechanacimientomod = datetime.strptime(fechanacimiento, '%Y-%m-%d').date()
        pais = request.form.get('Pais')
        email = request.form.get('Email')
        contraseña = request.form.get('Contraseña')
        esadmin = request.form.get('EsAdmin') == 'on'
        nuevo_usuario = Usuario(Nombre=nombre, Apellidos=apellidos, FechaNacimiento=fechanacimientomod, Pais=pais, Email=email, Contraseña=contraseña, EsAdmin=esadmin)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return redirect(url_for('BPusuarios.register_user'))
    es_admin = session.get('admin', False)
    return render_template('usuarios/gestionar_usuarios.html', es_admin=es_admin)

@BPusuarios.route('/user')
def user_profile():
    user = Usuario.query.get(1)
    if user:
        es_admin = session.get('admin', False)
        return render_template('usuarios/perfil.html', user=user, es_admin=es_admin)
    return "Usuario no encontrado", 404

@BPusuarios.route('/gestion_usuarios')
def gestion_usuarios():
    es_admin = session.get('admin', False)
    return render_template('usuarios/gestionar_usuarios.html', es_admin=es_admin)