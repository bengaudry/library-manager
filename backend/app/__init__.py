from flask import Flask
from flask_cors import CORS
from .models import Books
from .models import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/*": {"origins": "*"}})

    db.init_app(app)

    from .routes import api
    app.register_blueprint(api)

    with app.app_context():
        db.create_all()

        if Books.query.count() == 0:
            b1 = Books(title="1984", author="George Orwell", position="A1", exemplars=3)
            b2 = Books(title="Le Petit Prince", author="Antoine de Saint-Exupéry", position="B2", exemplars=2)
            b3 = Books(title="Dune", author="Frank Herbert", position="C3", exemplars=1)

            db.session.add_all([b1, b2, b3])
            db.session.commit()

    return app