import flask
from flask import jsonify, request
import sqlalchemy_serializer
import datetime
from . import db_session
from .news import News
from .jobs import Jobs
from .users import User
from flask import make_response
from . import parser as ps
from flask_restful import reqparse, abort, Api, Resource

db_session.global_init("db/register.db")


def abort_if_news_not_found(user_id):
    session = db_session.create_session()
    news = session.query(User).get(user_id)
    if not news:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        return jsonify({'users': users.to_dict(
            only=('name', 'surname', 'email', 'age', 'position', 'speciality', 'address'))})

    def delete(self, user_id):
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('name', 'surname', 'email', 'age', 'position', 'speciality', 'address')) for item in users]})

    def post(self):
        args = ps.parser.parse_args()
        session = db_session.create_session()
        users = User(
            name=args['name'],
            surname=args['surname'],
            email=args['email'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            hashed_password=args['password']
        )
        session.add(users)
        session.commit()
        return jsonify({'success': 'OK'})
