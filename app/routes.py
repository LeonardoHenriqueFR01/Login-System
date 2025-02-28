from flask import render_template, request, redirect, url_for, session, Blueprint
from .models import db, User
from time import sleep


main = Blueprint('main', __name__)


# Rota para página principal 
@main.route('/')
def home():
    sleep(3)
    return render_template('index.html')


# Rota para página apos fazer cadastro
@main.route('/sucess_cadastro')
def sucess_cadastro():
    return render_template('sucess_cadastro.html')


# Rota para página apos fazer login
@main.route('/sucess_login')
def sucess_login():
    return render_template('sucess_login.html')


# Rota para fazer cadastro 
@main.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        user_exists = User.query.filter_by(name=name, email=email).first()

        if user_exists:
            return redirect(url_for('main.home', error="Nome ou Email já cadastrado."))            
        else:
            user = User(name=name, email=email, password=password)

            db.session.add(user)
            db.session.commit()

            sleep(3)
            return redirect(url_for('main.sucess_cadastro', name=name))
    
    return render_template('index.html')


# Rota para fazer login
@main.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        name = request.form.get('name_login')
        email = request.form.get('email_login')
        password = request.form.get('password_login')

        user_exists = User.query.filter_by(name=name, email=email, password=password).first()

        if user_exists:
            sleep(3)
            return redirect(url_for('main.sucess_login', name=name))
        else:
            return redirect(url_for('main.home', error="Dados inválidos Tente novamente."))

    return render_template('index.html')
    