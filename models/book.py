from flask_restful import Resource
from flask_jwt import jwt_required
from flask import request
from models.db import db_connection

con = db_connection()


class Book(Resource):

    def get(self):
        sqlQuery = """SELECT * FROM books"""
        cur = con.execute(sqlQuery)
        return cur.fetchall()

    def post(self):
        book_id = request.form.get('book_id')
        title = request.form.get('title')
        author_name = request.form.get('author_name')
        isbn_num = request.form.get('isbn_num')
        genre = request.form.get('genre')
        description = request.form.get('description')

        sqlQuery = """INSERT INTO books (book_id, title, author_name, 
        isbn_num, genre, description) VALUES ()"""

        cur = con.execute(sqlQuery, (book_id, title, author_name,
        isbn_num, genre, description))

        con.commit()
        return f'Book added successfully', 200


    def delete(self):
        pass

    def put(self):
        pass



