from flask import Flask, jsonify, request

app = Flask(__name__)

# Memory Database
books = [
    {
        "id": 1,
        "book_name": "1984",
        "author": "George Orwell",
        "publisher": "Secker and Warburg"
    }
]

# GET Books
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

# GET by ID
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# CREATE a new book
@app.route("/books", methods=["POST"])
def add_book():
    new_book = {
        "id": request.json["id"],
        "book_name": request.json["book_name"],
        "author": request.json["author"],
        "publisher": request.json["publisher"]
    }
    books.append(new_book)
    return jsonify(new_book), 201

# UPDATE a book
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    for book in books:
        if book["id"] == book_id:
            book["book_name"] = request.json.get("book_name", book["book_name"])
            book["author"] = request.json.get("author", book["author"])
            book["publisher"] = request.json.get("publisher", book["publisher"])
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# DELETE a book
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return jsonify({"message": "Book deleted"})
    return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)