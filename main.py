from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    #db_session.global_init("db/blogs.db")
    #user = User()
    #user.surname = "Scott"
    #user.name = "Ridley"
    #user.age = 21
    #user.position = "captain"
    #user.speciality = "research engineer"
    #user.address = "module_1"
    #user.email = "scott_chief@mars.org"
    #user.hashed_password = "cap"
    #db_sess = db_session.create_session()
    #db_sess.add(user)
    #db_sess.commit()

    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Scott2"
    user.name = "Ridley2"
    user.age = 23
    user.position = "co-captain"
    user.speciality = "research engineer"
    user.address = "module_2"
    user.email = "scott2_co-chief@mars.org"
    user.hashed_password = "cap"
    session = db_session.create_session()
    session.add(user)
    session.commit()

    # app.run()


if __name__ == '__main__':
    main()
