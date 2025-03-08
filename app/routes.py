from flask import render_template, request, redirect, url_for, session, Blueprint  
from werkzeug.security import generate_password_hash, check_password_hash  
from .models import db, User  # Importa a instância do banco de dados e o modelo User  
from time import sleep  # Importa a função sleep para adicionar atrasos nas respostas  


# Criação do Blueprint 'main' para organizar as rotas
main = Blueprint('main', __name__)


# Rota para página principal  
@main.route('/')
def home():
    sleep(3)  # Adiciona um atraso de 3 segundos antes de renderizar a página  
    return render_template('index.html')  # Renderiza a página inicial  


# Rota para a página exibida após o cadastro bem-sucedido  
@main.route('/sucess_cadastro')
def sucess_cadastro():
    name = request.args.get('name')  # Obtém o nome do usuário passado via query string  
    return render_template('sucess_cadastro.html', name=name)  # Renderiza a página com o nome  


# Rota para a página exibida após o login bem-sucedido  
@main.route('/sucess_login')
def sucess_login():
    name = request.args.get('name')  # Obtém o nome do usuário passado via query string  
    return render_template('sucess_login.html', name=name)  # Renderiza a página com o nome  


# Rota para realizar o cadastro de usuários  
@main.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    error_message = None  # Variável para armazenar mensagens de erro  

    if request.method == "POST":  # Verifica se a requisição é do tipo POST  
        name = request.form.get('name')  # Obtém o nome do formulário  
        email = request.form.get('email')  # Obtém o email do formulário  
        password = request.form.get('password')  # Obtém a senha do formulário  

        # Verifica se já existe um usuário com o mesmo nome ou email  
        user_exists = User.query.filter((User.name == name) | (User.email == email)).first()  

        if user_exists:  
            error_message = "Nome ou Email já cadastrado!"  # Mensagem de erro caso o usuário já exista  
            return render_template('index.html', error_cadastro=error_message)  # Retorna à página inicial com erro  
        else:  
            senha_hash = generate_password_hash(password)  # Gera um hash seguro para a senha  
            user = User(name=name, email=email, password=senha_hash)  # Cria um novo usuário  

            db.session.add(user)  # Adiciona o usuário ao banco de dados  
            db.session.commit()  # Confirma a transação no banco  

            sleep(3)  # Adiciona um atraso de 3 segundos antes de redirecionar  
            return redirect(url_for('main.sucess_cadastro', name=name))  # Redireciona para a página de sucesso  
    
    return render_template('index.html')  # Renderiza a página inicial caso seja uma requisição GET  


# Rota para realizar login  
@main.route('/login', methods=['POST', 'GET'])
def login():
    error_message = None  # Variável para armazenar mensagens de erro  

    if request.method == "POST":  # Verifica se a requisição é do tipo POST  
        name = request.form.get('name_login')  # Obtém o nome do formulário  
        email = request.form.get('email_login')  # Obtém o email do formulário  
        password = request.form.get('password_login')  # Obtém a senha do formulário  

        # Verifica se o usuário existe no banco de dados  
        user_exists = User.query.filter_by(name=name, email=email).first()  

        # Verifica se o usuário existe e se a senha informada corresponde ao hash armazenado  
        if user_exists and check_password_hash(user_exists.password, password):  
            sleep(3)  # Adiciona um atraso de 3 segundos antes de redirecionar  
            return redirect(url_for('main.sucess_login', name=name))  # Redireciona para a página de sucesso  
        else:  
            error_message = "Dados inválidos! Tente novamente."  # Mensagem de erro caso os dados estejam errados  
            return render_template('index.html', error_login=error_message)  # Retorna à página inicial com erro  

    return render_template('index.html')  # Renderiza a página inicial caso seja uma requisição GET  
