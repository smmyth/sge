class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///estoque.db'  # Define o URI do banco de dados SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desativa notificações de modificações de objetos
    SECRET_KEY = 'sua_chave_secreta_aqui'  # Chave secreta para proteger sessões
