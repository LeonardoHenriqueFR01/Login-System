from flask_sqlalchemy import SQLAlchemy  # Importa a extensão SQLAlchemy para gerenciar o banco de dados

db = SQLAlchemy()  # Cria uma instância do banco de dados SQLAlchemy

class User(db.Model):  # Define a classe User como um modelo do banco de dados
    __tablename__ = 'Users'  # Nome da tabela no banco de dados

    # Definição das colunas da tabela Users
    id = db.Column(db.Integer, primary_key=True)  # Chave primária, identificador único para cada usuário
    name = db.Column(db.String(140), unique=True, nullable=False)  # Nome do usuário (único e obrigatório)
    email = db.Column(db.String(140), unique=True, nullable=False)  # Email do usuário (único e obrigatório)
    password = db.Column(db.String(350), nullable=False)  # Senha do usuário (obrigatória)

    def __repr__(self):
        """Representação da instância do objeto User como string"""
        return f"<User {self.name}, {self.email}>"  

    def asdict(self):
        """Retorna um dicionário contendo alguns atributos do usuário"""
        return {
            "id": self.id,
            "name": self.name
        }
