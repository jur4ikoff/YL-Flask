from data import db_session, news_api
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/register.db")
    app.register_blueprint(news_api.blueprint)
    app.run(port=8081, host='127.0.0.1')


if __name__ == '__main__':
    main()
