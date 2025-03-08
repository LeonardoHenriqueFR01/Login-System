from flask import Flask  # Importa a classe Flask para criar a aplicação web
from .models import db  # Importa a instância do banco de dados definida em models.py


def create_app():
    app = Flask(__name__)  # Cria a instância do aplicativo Flask

    # Configurações do banco de dados SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa notificações de modificações no SQLAlchemy (evita consumo extra de memória)

    db.init_app(app)  # Inicializa a instância do banco de dados com o aplicativo Flask

    # Importa e registra as rotas definidas no módulo routes.py
    from .routes import main  
    app.register_blueprint(main)  # Registra um blueprint para modularizar as rotas

    with app.app_context():  # Cria um contexto da aplicação para executar operações do banco de dados
        db.create_all()  # Cria todas as tabelas do banco de dados, se ainda não existirem
    
    return app  # Retorna a instância do aplicativo Flask
