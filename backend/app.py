from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

books = [
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "location": "A1",
        "available": True
    },
    {
        "id": 2,
        "title": "Le Petit Prince",
        "author": "Antoine de Saint-Exupéry",
        "location": "B2",
        "available": False
    },
    {
        "id": 3,
        "title": "Dune",
        "author": "Frank Herbert",
        "location": "C3",
        "available": True
    }
]

@app.route("/books")
def get_books():
    return jsonify(books)

@app.route("/")
def home():
    return {"status": "Backend OK"}

if __name__ == "__main__":
    app.run(port=5000, debug=True)