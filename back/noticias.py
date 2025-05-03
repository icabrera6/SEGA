from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BibliotecaCapitan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Noticia(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Juego = db.Column(db.String(50), nullable=True)
    Titulo = db.Column(db.String(50), nullable=True)
    Texto = db.Column(db.String(1000), nullable=True)

# Crear noticia
@app.route('/signup', methods=['GET', 'POST'])
def add_noticia():
    if request.method == 'POST':
        Id = request.form.get('id')
        Juego = request.form.get('juego')
        Titulo = request.form.get('titulo')            
        Texto = request.form.get('texto')
        new_noticia = Noticia(Id=Id, Juego=Juego, Titulo=Titulo, Texto=Texto)
        db.session.add(new_noticia)
        db.session.commit()
        return redirect(url_for('noticias')) 
    return render_template('new_libro.html')  

@app.route('/noticias')
def noticias():
    todas = Noticia.query.all()
    return render_template('noticias.html', noticias=todas)

# Eliminar noticia
@app.route('/noticia/delete/<int:noticia_id>', methods=['POST'])
def delete_noticia(noticia_id):
    noticia = Noticia.query.get(noticia_id)
    if noticia:
        db.session.delete(noticia)
        db.session.commit()
        return f"Mensaje: La noticia con el ID {noticia_id} ha sido eliminada correctamente."
    else:
        return jsonify({"error": "Noticia no encontrada"}), 404

# Editar noticia
@app.route('/noticia/edit/<int:noticia_id>', methods=['GET', 'POST'])
def edit_noticia(noticia_id):
    noticia = Noticia.query.get_or_404(noticia_id)
    if request.method == 'POST':
        noticia.Juego = request.form.get('juego')
        noticia.Titulo = request.form.get('titulo')
        noticia.Texto = request.form.get('texto')
        db.session.commit()
        return redirect(url_for('noticias')) 

    return render_template('edit_libro.html', noticia=noticia) 
