from flask import Flask
from controllers.usuario_controller import usuario_bp
from config import Config
#from controllers.cliente_controller import cliente_bp
#from controllers.produto_controller import produto_bp
#from controllers.pedido_controller import pedido_bp
from models import db

def criar_app():
# Inicializando o aplicativo Flask
    app = Flask(__name__)

# Configurando a conexão com o banco de dados
    app.config.from_object(Config)
   
    db.init_app(app)

# Registrando os blueprints para modularizar as rotas
    app.register_blueprint(usuario_bp)
#app.register_blueprint(cliente_bp)
#app.register_blueprint(produto_bp)
##app.register_blueprint(pedido_bp)

    with app.app_context():
        db.create_all()  # Cria todas as tabelas definidas nos modelos

    app.run(debug=True)


if __name__ == '__main__':
       app = criar_app()  # Inicia o servidor em modo de depuração
