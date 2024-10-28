from flask import Blueprint, render_template, request, redirect, url_for
from models.detalhe_pedido import DetalhePedido
from models.produto import Produto
from app import db

# Criando um blueprint para as rotas de pedido
pedido_bp = Blueprint('pedido', __name__)

@pedido_bp.route('/pedidos', methods=['GET', 'POST'])
def gerenciar_pedidos():
    if request.method == 'POST':
        # Recebe dados do formulário e cria um novo detalhe de pedido
        produto_id = request.form['produto_id']
        quantidade = int(request.form['quantidade'])
        preco = float(request.form['preco'])
        desconto = float(request.form['desconto'])
        pedido_id = request.form['pedido_id']  # ID do pedido associado (deve ser gerenciado adequadamente)

        # Cria um novo detalhe de pedido
        detalhe = DetalhePedido(pedido_id=pedido_id, produto_id=produto_id, quantidade=quantidade, preco=preco, desconto=desconto)
        db.session.add(detalhe)  # Adiciona o detalhe à sessão do banco de dados
        db.session.commit()  # Salva as alterações
        return redirect(url_for('pedido.gerenciar_pedidos'))  # Redireciona para a lista de pedidos

    # Obtém todos os produtos e detalhes de pedido do banco de dados
    produtos = Produto.query.all()
    detalhes = DetalhePedido.query.all()
    return render_template('pedidos.html', detalhes=detalhes, produtos=produtos)  # Renderiza a página de pedidos
