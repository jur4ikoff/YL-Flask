import datetime
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username1 = StringField('id капитана', validators=[DataRequired()])
    password1 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


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


@app.route('/')
def index():
    return '''hello world'''


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
        return redirect('/success')
    return render_template('form.html', title='Двойная защита', form=form)


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


if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')
    # main()
