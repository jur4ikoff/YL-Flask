import datetime

from flask import Flask
from data import db_session
from data.news import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    # db_session.global_init("db/blogs.db")
    # user = User()
    # user.surname = "Scott"
    # user.name = "Ridley"
    # user.age = 21
    # user.position = "captain"
    # user.speciality = "research engineer"
    # user.address = "module_1"
    # user.email = "scott_chief@mars.org"
    # user.hashed_password = "cap"
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()

    db_session.global_init("db/blogs.db")
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = '15'
    job.collaborators = '2, 3'
    job.start_date = datetime.datetime.now()
    job.is_finished = False
    session = db_session.create_session()
    session.add(job)
    session.commit()

    # app.run()


if __name__ == '__main__':
    main()
