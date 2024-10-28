from flask import Blueprint, render_template, request, redirect, url_for
from models.produto import Produto
from app import db

# Criando um blueprint para as rotas de produto
produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/produtos', methods=['GET', 'POST'])
def gerenciar_produtos():
    if request.method == 'POST':
        # Recebe dados do formulário e cria um novo produto
        nome = request.form['nome']
        preco = float(request.form['preco'])
        quantidade = int(request.form['quantidade'])
        novo_produto = Produto(nome=nome, preco=preco, quantidade=quantidade)
        db.session.add(novo_produto)  # Adiciona o produto à sessão do banco de dados
        db.session.commit()  # Salva as alterações
        return redirect(url_for('produto.gerenciar_produtos'))  # Redireciona para a lista de produtos
    
    # Obtém todos os produtos do banco de dados
    produtos = Produto.query.all()
    return render_template('produtos.html', produtos=produtos)  # Renderiza a página de produtos
