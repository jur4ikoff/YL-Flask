import flask
from flask import jsonify, request
import sqlalchemy_serializer
import datetime
from . import db_session
from .news import News
from .jobs import Jobs
from .users import User
from flask import make_response
from . import parser1 as ps
from flask_restful import reqparse, abort, Api, Resource

db_session.global_init("db/register.db")


def abort_if_news_not_found(jobs_id):
    session = db_session.create_session()
    news = session.query(User).get(jobs_id)
    if not news:
        abort(404, message=f"Job {jobs_id} not found")


class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_news_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        return jsonify({'jobs': jobs.to_dict(
            only=('team_leader', 'job', 'work_size', 'collaborators', 'is_finished'))})

    def delete(self, jobs_id):
        abort_if_news_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'users': [item.to_dict(
            only=('team_leader', 'job', 'work_size', 'collaborators', 'is_finished')) for item in jobs]})

    def post(self):
        args = ps.parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished'])
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})
