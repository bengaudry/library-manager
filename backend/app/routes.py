from flask import Blueprint, jsonify, request
from .models import db, Books
from .auth import is_username_and_password_correct, create_or_replace_session_for_user, delete_session, verify_session

api = Blueprint('api', __name__)

@api.route('/books', methods=['GET'])
def get_books():
    books = db.session.query(Books).all()
    return jsonify([b.to_dict() for b in books])


@api.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = db.session.query(Books).get(book_id)
    if book is None:
        return jsonify({"error": "Livre non trouvé"}), 404
    return jsonify(book.to_dict())

@api.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Books(title=data['title'], author=data['author'], position=data['position'], exemplars=data['exemplars'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@api.route('/sessions', methods=['POST'])
def login():
    data = request.get_json()
    user_name=data['user_name']
    password = data['password']
    if is_username_and_password_correct(user_name, password): # Si username et mot de passe sont correct
        token = create_or_replace_session_for_user(user_name)
        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Incorrect username or password"}), 401

@api.route('/sessions/<int:token>', methods=['GET'])
def verify_token(token):
    if verify_session(token):
        return jsonify({"success": "you are logged in"}), 200
    else:
        return jsonify({"error": "Incorrect token"}), 401

@api.route('/sessions/<int:token>', methods=['DELETE'])
def logout(token):
    if verify_session(token):
        delete_session(token)
        return jsonify({"success": "you are logged out"}), 200
    else:
        return jsonify({"error": "Incorrect token"}), 401

@api.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    # Informations manquantes
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({"erreur": "Veuillez remplir tout le formulaire !"}), 400

    # Vérifie si l'email n'est pas déjà lié à un compte
    existing_email = User.query.filter_by(email=data['email']).first()
    if existing_email:
        return jsonify({"erreur": "L'e-mail est déjà lié à un compte !'"}), 400

    # Vérifie si le nom d'utilisateur n'est pas déjà utilisé
    existing_username = User.query.filter_by(username=data['username']).first()
    if existing_username:
        return jsonify({"erreur": "Le nom d'utilisateur est déjà utilisé !"}), 400

    # Création du nouvel utilisateur
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Utilisateur créé avec succès !", "user": new_user.to_dict()}), 201