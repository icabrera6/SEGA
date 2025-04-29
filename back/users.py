from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BibliotecaCapitan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)

class User(db.Model):
    Id= db.Column(db.Integer, primary_key=True)
    Fecha_nacimiento= db.Column(db.Date, nullable=True)
    Nombre= db.Column(db.String(50), nullable=True)
    Apellidos= db.Column(db.String(50), nullable=True)
    Pais= db.Column(db.String(50), nullable=True)
    Gmail= db.Column(db.String(50), nullable=True)


    #Add user
@app.route('/signup', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        Id = request.form.get('id')
        Fecha_nacimiento = request.form.get('fecha_nacimiento')
        Nombre = request.form.get('nombre')
        Apellidos = request.form.get('apellidos')            
        Pais= request.form.get('pais')
        Gmail= request.form.get('gmail')
        new_user = User(id=id, fecha_nacimiento=Fecha_nacimiento, Nombre=Nombre, Apellidos=Apellidos, Pais=Pais, Gmail=Gmail)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('get_libros'))
        
        return render_template('new_libro.html')

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == "POST":
        gmail = request.form.get('gmail')
        user = User.query.filter_by(gmail=gmail).first()
        if user:
            return redirect(url_for('user_profile', user_id=user.id)) 
        else:
            return render_template('user_profile_failed.html')
    return render_template('sesion.html')

# Perfil de usuario
@app.route('/user/<int:user_id>')
def user_profile(user_id):
    user = User.query.get(user_id)
    if user:
        return render_template('user_profile.html', user=user)
    else:
        return render_template('user_profile_failed.html')

if __name__ == '__main__':
    app.run(debug=True)