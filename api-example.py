import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {
        'title': 'A Book',
        'author': 'Kris'
    },
    {
        'title': 'This book',
        'author': 'Mary'
    }
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello World!</h1><p>From Python and Flask!</p>"


@app.route('/api/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


app.run()
