from flask import Blueprint, render_template, request, redirect, url_for
from models.cliente import Cliente
from app import db

# Criando um blueprint para as rotas de cliente
cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/clientes', methods=['GET', 'POST'])
def gerenciar_clientes():
    if request.method == 'POST':
        # Recebe dados do formulário e cria um novo cliente
        nome = request.form['nome']
        email = request.form['email']
        novo_cliente = Cliente(nome=nome, email=email)
        db.session.add(novo_cliente)  # Adiciona o cliente à sessão do banco de dados
        db.session.commit()  # Salva as alterações
        return redirect(url_for('cliente.gerenciar_clientes'))  # Redireciona para a lista de clientes
    
    # Obtém todos os clientes do banco de dados
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)  # Renderiza a página de clientes
