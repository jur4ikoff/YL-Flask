from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index1():
    return "Миссия Колонизация Марса"


@app.route('/index/<name>')
def index(name):
    user = "Ученик Яндекс.Лицея"
    return render_template('base.html', title=name)


@app.route('/training/<prof>')
def training(prof):
    print(url_for('static', filename='img/mars2.jpeg'))
    return render_template('index.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
