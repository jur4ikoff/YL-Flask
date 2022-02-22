from flask import *

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index1():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства. </br>

            Человечеству мала одна планета. </br>

Мы сделаем обитаемыми безжизненные пока планеты. </br>

И начнем с Марса! </br>

Присоединяйся!
    """


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <title>Варианты выбора</title>
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/red.css')}" />
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                          </head>
                          <body>
                            <h1>Результаты отбора</h1>                                                                                                                    
                            <div>
                              <h2>Претендента на участие в миссии {nickname}:</h2>
                            </div>
                            <div class="alert alert-success" role="alert">
                              Поздравляем! Ваш рейтинг после {level} этапа отбора
                            </div>
                            <div>
                              составляет {rating}!
                            </div>
                            </div>
                            <div class="alert alert-warning" role="alert">
                               Желаем удачи!
                            </div>
                          </body>
                        </html>'''


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <title>Пейзажи марса</title>
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/red.css')}" />
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet" 
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                crossorigin="anonymous">
                              </head>
                              <body>
                                <h1 align="center">HTML заголовок справа</h1>
                                <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                                  <div class="carousel-inner">
                                    <div class="carousel-item active">
                                      <img class="d-block w-100" src="{url_for('static', filename='img/Mars.png')}" alt="First slide">
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block w-100" src="{url_for('static', filename='img/mars1.png')}" alt="Second slide">
                                    </div>
                                    <div class="carousel-item">
                                      <img class="d-block w-100" src="{url_for('static', filename='img/mars2.png')}" alt="Third slide">
                                    </div>
                                  </div>
                                  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                    <span class="sr-only">Previous</span>
                                  </a>
                                  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                    <span class="sr-only">Next</span>
                                  </a>
                                </div>                                                                                                                
                              </body>
                            </html>'''


if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')
