from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username1 = StringField('id капитана', validators=[DataRequired()])
    password1 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/')
def index():
    return '''hello world'''


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
        # return redirect('/success')
    return render_template('form.html', title='Двойная защита', form=form)


@app.route('/distribution')
def distribution():
    return render_template('cabins.html', title='по каютам')


@app.route('/table/<sex>/<age>')
def table(sex, age):
    return render_template('color_cabin.html', title='Цвет каюты', sex=sex, age=age)


if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')
