from flask import Blueprint, jsonify, request
from .models import db, Books
from flask_cors import CORS

api = Blueprint('api', __name__)
CORS(api)

@api.route('/books', methods=['GET'])
def get_books():
    books = db.session.query(Books).all()
    return jsonify([b.to_dict() for b in books])

@api.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Books(title=data['title'], author=data['author'], position=data['position'], exemplars=data['exemplars'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@api.route('/reserve/<int:book_id>', methods=['POST'])
def reserve_book(book_id):
    book = db.session.get(Books, book_id)
    if not book:
        return jsonify({"error": "Livre introuvable"}), 404

    if book.exemplars > 0:
        book.exemplars -= 1
        db.session.commit()
        return jsonify(book.to_dict())

    return jsonify({"error": "Indisponible"}), 400