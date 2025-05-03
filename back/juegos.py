from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BibliotecaCapitan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de la base de datos
class Juego(db.Model):
    IdJuego = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50), nullable=True)
    Genero = db.Column(db.String(50), nullable=True)
    Descripcion = db.Column(db.String(50), nullable=True)
    Imagen = db.Column(db.String(50), nullable=True)

# Ruta para añadir juegos
@app.route('/añadir_juego', methods=["GET", "POST"])
def add_game():
    if request.method == 'POST':
        id = request.form.get('idjuego')
        nombre = request.form.get('nombre')
        genero = request.form.get('genero')
        descripcion = request.form.get('descripcion')
        imagen = request.form.get('imagen')

        nuevo_juego = Juego(IdJuego=id, Nombre=nombre, Genero=genero,
                            Descripcion=descripcion, Imagen=imagen)
        db.session.add(nuevo_juego)
        db.session.commit()

        return redirect(url_for('add_game'))  # Redirige a la misma página

    return render_template('add.html')

# Solo se ejecuta si corres este archivo directamente
if __name__ == '__main__':
    # Crear las tablas si no existen
    with app.app_context():
        db.create_all()
    app.run(debug=True)
