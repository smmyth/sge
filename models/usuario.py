from . import db

class Usuario(db.Model):
    # Modelo para a tabela de usuários
    id = db.Column(db.Integer, primary_key=True)  # Identificador único
    username = db.Column(db.String(80), unique=True, nullable=False)  # Nome de usuário único
    senha = db.Column(db.String(120), nullable=False)  # Senha do usuário
