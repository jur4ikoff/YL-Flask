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
    return render_template('index2.html', prof=prof)


@app.route('/list_prof/<param>')
def proffesions(param):
    list_prof = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог',
                 'врач', 'инженер по терраформированию', 'климатолог',
                 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                 'инжинер жизнеобеспечения', 'метеоролог', 'оператор марсохода',
                 'киберинженер', 'штурман', 'пилот дронов']
    return render_template('index.html', prof=param, news=list_prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
