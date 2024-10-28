from flask import Blueprint, render_template, request, redirect, url_for
from models.usuario import Usuario
from models import db

# Criando um blueprint para as rotas de usuário
usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/usuarios', methods=['GET', 'POST'])
def gerenciar_usuarios():
    if request.method == 'POST':
        # Recebe dados do formulário e cria um novo usuário
        username = request.json['username']
        senha = request.json['senha']
        novo_usuario = Usuario(username=username, senha=senha)
        db.session.add(novo_usuario)  # Adiciona o usuário à sessão do banco de dados
        db.session.commit()  # Salva as alterações
        return redirect(url_for('usuario.gerenciar_usuarios'))  # Redireciona para a lista de usuários
    
    # Obtém todos os usuários do banco de dados
    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)  # Renderiza a página de usuários
