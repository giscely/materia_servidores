from flask import Flask, request, render_template, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'VASCO'

DATABASE = 'database/database.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    user_name = session.get('user')
    return render_template('index.html', user_name=user_name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        conn = get_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()
        if user and check_password_hash(user['senha'], senha):
            session['user'] = user['nome'] 
            return redirect(url_for('index'))
        else:
            flash('Email ou senha inválido!')
    if 'user' in session:
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None) 
    return redirect(url_for('index'))


@app.route('/cadastro', methods=['POST','GET'])
def cadastro():
    if request.method == 'POST':
        try:
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']
            hash = generate_password_hash(senha) 
            conn = get_connection()
            conn.execute('INSERT INTO users(nome,email,senha) VALUES (?,?,?)',(nome,email,hash))
            conn.commit()
            user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
            conn.close()
            session['user'] = user['nome'] 
            return redirect(url_for('index'))    
        except sqlite3.IntegrityError:
            flash('Email já cadastrado!')
        finally:
            conn.close()
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run()