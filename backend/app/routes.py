from flask import Blueprint, jsonify, request
from .models import db, Books

api = Blueprint('api', __name__)

@api.route('/books', methods=['GET'])
def get_books():
    books = db.session.query(Books).all()
    return jsonify([b.to_dict() for b in books])

@api.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Books(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201