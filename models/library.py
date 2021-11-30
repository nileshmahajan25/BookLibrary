from flask_restful import Resource
from flask_jwt import jwt_required
from flask import request
from models.db import db_connection

con = db_connection()

class LibraryBooks(Resource):

    def post(self):
        '''
        Enter book entry
        :return:
        '''
        library_book_id = request.form.get('library_book_id')
        library_id = request.form.get('library_id')
        book_id = request.form.get('book_id')
        last_library_activity_id = request.form.get('last_library_activity_id')

        sqlQuery = """INSERT INTO library_books (
        library_book_id, library_id, book_id, last_library_activity_id) 
        VALUES (?, ?, ?, ?)"""

        cur = con.execute(sqlQuery, (library_book_id, library_id, book_id, last_library_activity_id))
        con.commit()

        return f"Book id : {cur.lastrowid} added successfully"



class LibraryActivity(Resource):

    def post(self, book_id):
        '''
        Creating entry for book
        :param book_id:
        :return:
        '''
        library_activity_id = request.form.get('library_activity_id')
        activity_type = request.form.get('activity_type')
        user_id = request.form.get('user_id')
        library_book_id = request.form.get('library_book_id')
        checked_out_at = request.form.get('checked_out_at')
        checked_in_at = request.form.get('checked_in_at')

        sqlQuery = """INSTER INTO library_activities (
        library_activity_id, activity_type, user_id, library_book_id, 
        checked_out_at, checked_in_at) VALUES (?, ?, ?, ?, ?, ?)"""

        cur = con.execute(sqlQuery, (library_activity_id, activity_type, user_id,
                                     library_book_id, checked_out_at, checked_in_at))

        con.commit()
        return f'Library activity added successfully', 200


    def put(self, book_id):
        '''
        Create outtime for book
        :param book_id:
        :return:
        '''
        pass