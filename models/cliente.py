from . import db

class Cliente(db.Model):
    # Modelo para a tabela de clientes
    id = db.Column(db.Integer, primary_key=True)  # Identificador único
    nome = db.Column(db.String(120), nullable=False)  # Nome do cliente
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email único do cliente

    def __repr__(self):
        return f'Cliente({self.nome}, {self.email})'  # Representação do objeto Cliente
