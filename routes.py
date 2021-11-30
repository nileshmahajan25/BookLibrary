from flask import Flask
from flask_restful import Resource, Api
from models.book import Book, BookLibrary
from models.libraries import Libraries

app = Flask(__name__)
api = Api(app)

api.add_resource(Book, '/book')
api.add_resource(BookLibrary, '/booklibrary')
api.add_resource(Libraries, '/libraries')

app.run(port=5000)
