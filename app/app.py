import os
import psycopg2
import bcrypt
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
# Lectura segura de credenciales desde variables de entorno
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('POSTGRES_DB'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD'),
        port=os.environ.get('DB_PORT')
    )

@app.route('/', methods=['GET', 'POST'])
def login():
    if 'usuario' in session:
        return redirect(url_for('bienvenida'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()
        
        # Consulta SQL parametrizada para evitar Inyección SQL (%s)
        cur.execute('SELECT password_hash, nombre_completo FROM usuarios WHERE username = %s', (username,))
        user = cur.fetchone()
        
        cur.close()
        conn.close()

        if user:
            stored_hash = user[0]
            nombre_completo = user[1]
            
            # Verificación criptográfica con bcrypt
            if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
                session['usuario'] = nombre_completo
                return redirect(url_for('bienvenida'))
            else:
                flash('Credenciales inválidas. Inténtelo de nuevo.', 'danger')
        else:
            flash('Credenciales inválidas. Inténtelo de nuevo.', 'danger')

    return render_template('login.html')

@app.route('/bienvenida')
def bienvenida():
    # Bloqueo de página protegida si no hay sesión activa
    if 'usuario' not in session:
        flash('Acceso denegado: Por favor, inicie sesión primero.', 'warning')
        return redirect(url_for('login'))
    
    return render_template('bienvenida.html', nombre=session['usuario'])

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
