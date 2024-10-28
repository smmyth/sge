from . import db

class DetalhePedido(db.Model):
    # Modelo para a tabela de detalhes do pedido
    id = db.Column(db.Integer, primary_key=True)  # Identificador único
    pedido_id = db.Column(db.Integer, nullable=False)  # ID do pedido associado
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)  # Referência ao produto
    quantidade = db.Column(db.Integer, nullable=False)  # Quantidade do produto no pedido
    preco = db.Column(db.Float, nullable=False)  # Preço do produto no momento do pedido
    desconto = db.Column(db.Float, default=0.0)  # Desconto aplicado ao produto

    produto = db.relationship('Produto', backref='detalhes')  # Relacionamento com o modelo Produto

    def __repr__(self):
        return f'DetalhePedido(pedido_id={self.pedido_id}, produto_id={self.produto_id}, quantidade={self.quantidade})'  # Representação do objeto DetalhePedido
