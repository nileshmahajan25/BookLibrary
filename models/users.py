from flask_restful import Resource
from flask_jwt import jwt_required
from flask import request
from models.db import db_connection

con = db_connection()

class Users(Resource):

    def post(self, user):
        '''
        Add new user into database
        :param user: User name
        :return:
        '''
        user_id = request.form.get('user_id')
        name = request.form.get('name')

        sqlQuery = """INSERT INTO users (user_id, name) VALUES (?, ?)"""

        cur = con.execute(sqlQuery, (user_id, name))
        con.commit()
        return f"User id : {cur.lastrowid} added successfully ", 200