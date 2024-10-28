from . import db

class Produto(db.Model):
    # Modelo para a tabela de produtos
    id = db.Column(db.Integer, primary_key=True)  # Identificador único
    nome = db.Column(db.String(120), nullable=False)  # Nome do produto
    preco = db.Column(db.Float, nullable=False)  # Preço do produto
    quantidade = db.Column(db.Integer, default=0)  # Quantidade em estoque

    def __repr__(self):
        return f'Produto({self.nome}, R$ {self.preco}, {self.quantidade} em estoque)'  # Representação do objeto Produto
