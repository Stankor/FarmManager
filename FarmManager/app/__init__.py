from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import api
    api.init_app(app)

# Registrar modelos (importar as classes de modelo)
    with app.app_context():
        from app.models import Fazenda, Animal, HistoricoPeso, Vacina, Inseminacao
        db.create_all()  # Cria as tabelas no banco, caso ainda não existam

    return app
