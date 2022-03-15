import datetime
from flask import Flask, render_template, redirect, request, make_response, url_for, abort
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField
from flask.sessions import *
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from data import db_session, news_api, jobs_api
from data.users import User
from data.news import News
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

def api():
    db_session.global_init("db/register.db")
    app.register_blueprint(news_api.blueprint)


def db_create():
    db_session.global_init("db/register.db")
    job = News()
    job.title = 'Test1'
    job.content = 'Test1 content'
    job.is_private = False
    job.user_id = 1
    job.created_date = datetime.datetime.now()
    session = db_session.create_session()
    session.add(job)
    session.commit()


class AddWork(FlaskForm):
    job = StringField('Название', validators=[DataRequired()])
    work_size = StringField("Продолжительность", validators=[DataRequired()])
    collaborators = StringField("Список id команды", validators=[DataRequired()])
    is_finished = BooleanField('Завершена ли работа?')
    submit = SubmitField('Применить')


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание")
    is_private = BooleanField("Личное")
    submit = SubmitField('Применить')


class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    email = StringField('login/email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Confirm password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = StringField("Age")
    position = StringField("position")
    speciality = StringField("Speciality")
    address = StringField("Address")
    submit = SubmitField('Войти')


@app.route('/edit_job/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_works_log(id):
    form = AddWork()
    if request.method == "GET":
        session = db_session.create_session()
        jobs = session.query(Jobs).filter(Jobs.id == id, ((Jobs.team_leader == current_user.id) |
                                                          (current_user.id == 1))).first()
        if jobs:
            form.job.data = jobs.job
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.is_finished.data = jobs.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        session = db_session.create_session()
        jobs = session.query(Jobs).filter(Jobs.id == id, ((Jobs.team_leader == current_user.id) |
                                                          (current_user.id == 1))).first()
        if jobs:
            jobs.job = form.job.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            jobs.is_finished = form.is_finished.data
            session.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('jobs.html', title='Редактирование', form=form)


@app.route('/del_job/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_job(id):
    session = db_session.create_session()
    jobs = session.query(Jobs).filter(Jobs.id == id, ((Jobs.team_leader == current_user.id) |
                                                      (current_user.id == 1))).first()
    if jobs:
        session.delete(jobs)
        session.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/')
def works_logs():
    db_session.global_init("db/register.db")
    session = db_session.create_session()
    job = session.query(Jobs)
    return render_template("index_jobs.html", job=job)


@app.route('/add_job', methods=['GET', 'POST'])
@login_required
def add_job():
    form = AddWork()
    if form.validate_on_submit():
        session = db_session.create_session()
        jobs = Jobs()
        jobs.job = form.job.data
        jobs.team_leader = current_user.id
        jobs.work_size = form.work_size.data
        jobs.collaborators = form.collaborators.data
        jobs.is_finished = form.is_finished.data
        current_user.jobs.append(jobs)
        session.merge(current_user)
        session.commit()
        return redirect('/')
    return render_template('jobs.html', title='Добавление', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/news')
def index():
    db_session.global_init("db/register.db")
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


@app.route('/login', methods=['GET', 'POST'])
def login():
    db_session.global_init("db/register.db")
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    return render_template('cabins.html', title='по каютам')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    db_session.global_init("db/register.db")
    session = db_session.create_session()
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User()
        user.email = form.email.data
        user.surname = form.surname.data
        user.name = form.name.data
        user.age = form.age.data
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.address = form.address.data
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/sample_page')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/gray_title.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                  </body>
                </html>"""


@app.route("/cookie_test")
def cookie_test():
    visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(render_template('cookie_test.html', title='cookie test', visits_count=visits_count))
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response(
            "Вы пришли на эту страницу в первый раз за последние 2 года")
        res.set_cookie("visits_count", '1',
                       max_age=60 * 60 * 24 * 365 * 2)
    return res


@app.route('/add_news', methods=['GET', 'POST'])
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.append(news)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/news')
    return render_template('news.html', title='Добавление новости',
                           form=form)


@app.route('/news_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id,
                                      News.user == current_user
                                      ).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/news/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = NewsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user
                                          ).first()
        if news:
            form.title.data = news.title
            form.content.data = news.content
            form.is_private.data = news.is_private
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user
                                          ).first()
        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            db_sess.commit()
            return redirect('/news')
        else:
            abort(404)
    return render_template('news.html',
                           title='Редактирование новости',
                           form=form
                           )


if __name__ == '__main__':
    api()
    app.run(port=8070, host='127.0.0.1')
    #
