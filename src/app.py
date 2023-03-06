import http.client
import logging
import prometheus_client as prom
from random import randint
from time import sleep
from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

app = Flask(__name__)
metrics = PrometheusMetrics(app)

quantidade_usuarios_online = prom.Gauge('quantidade_usuarios_online', 'Número de usuários online')


def parametros_endpoint():
    sleep(randint(1, 10))
    quantidade_usuarios_online.set(randint(1, 100))


@app.route('/')
def index():
    return '<h1>Home! Olá, mundo :)</h1>'


@app.route('/renda-fixa')
def renda_fixa():
    app.logger.info('Acessando Renda Fixa!')
    parametros_endpoint()
    if randint(0, 1) == 0:
        return http.client.BAD_REQUEST
    return render_template('lista.html', titulo='Renda Fixa')


@app.route('/renda-variavel')
def renda_variavel():
    app.logger.info("%s %s %s %s", request.remote_addr, request.method,
                    request.scheme, request.full_path)
    parametros_endpoint()
    if randint(0, 1) == 0:
        return http.client.BAD_REQUEST
    return render_template("lista.html", titulo="Renda Variável")


@app.route('/acoes')
def acoes():
    app.logger.info("%s %s %s %s", request.remote_addr, request.method,
                    request.scheme, request.full_path)
    parametros_endpoint()
    if randint(0, 1) == 0:
        return http.client.BAD_REQUEST
    return render_template("lista.html", titulo="Ações")


@app.route('/fiis')
def fiis():
    app.logger.info("%s %s %s %s", request.remote_addr, request.method,
                    request.scheme, request.full_path)
    parametros_endpoint()
    if randint(0, 1) == 0:
        return http.client.BAD_REQUEST
    return render_template("lista.html", titulo="Fundo de Investimento Imobiliário")


@app.route('/criptos')
def criptos():
    app.logger.info("%s %s %s %s", request.remote_addr, request.method,
                    request.scheme, request.full_path)
    parametros_endpoint()
    if randint(0, 1) == 0:
        return http.client.BAD_REQUEST
    return render_template("lista.html", titulo="Criptos")


if __name__ == "__main__":
    app.run(host="0.0.0.0")  # porta = 5000

