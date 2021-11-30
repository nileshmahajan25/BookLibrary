from flask_restful import Resource
from flask_jwt import jwt_required
from flask import request
from models.db import db_connection

con = db_connection()

class Libraries(Resource):

    def post(self):
        '''
        Enter book entry
        :return:
        '''
        library_id = request.form.get('library_id')
        name = request.form.get('name')
        city = request.form.get('city')
        state = request.form.get('state')
        postal_code = request.form.get('postal_code')

        sqlQuery = """INSERT INTO libraries (
        library_id, name, city, state, postal_code) VALUES (?, ?, ?, ?, ?)"""

        cur = con.execute(sqlQuery, (library_id, name, city, state, postal_code))
        con.commit()
        return f"Library with the id : {cur.lastrowid} added successfully!"

