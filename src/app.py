import http.client
import logging
import prometheus_client as prom
from random import randint
from time import sleep
from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics

# configure the logger
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S')
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
# @metrics.counter('efetivacao_renda_fixa',
#                  'Número de papeis de renda fixa efetivados',
#                  labels={'tipo': 'RENDA FIXA'})
def renda_fixa():
    app.logger.info('Acessando Renda Fixa!')
    parametros_endpoint()
    if randint(0, 1) == 0:
        return http.client.BAD_REQUEST
    return render_template('lista.html', titulo='Renda Fixa')


@app.route('/renda-variavel')
# @metrics.counter('efetivacao_renda_variavel',
#                  'Número de papeis de renda variável efetivados',
#                  labels={'tipo': 'RENDA VARIÁVEL'})
def renda_variavel():
    app.logger.info("%s %s %s %s", request.remote_addr, request.method,
                    request.scheme, request.full_path)
    parametros_endpoint()
    if randint(0, 1) == 0:
        return http.client.BAD_REQUEST
    return render_template("lista.html", titulo="Renda Variável")


@app.route('/acoes')
# @metrics.counter('efetivacao_acoes',
#                  'Número de papeis de ações efetivadas',
#                  labels={'tipo': 'ACOES'})
def acoes():
    app.logger.info("%s %s %s %s", request.remote_addr, request.method,
                    request.scheme, request.full_path)
    parametros_endpoint()
    if randint(0, 1) == 0:
        return http.client.BAD_REQUEST
    return render_template("lista.html", titulo="Ações")


@app.route('/fiis')
# @metrics.counter('efetivacao_fiis',
#                  'Número de papeis de fundos de investimento imobiliário efetivados',
#                  labels={'tipo': 'FIIS'})
def fiis():
    app.logger.info("%s %s %s %s", request.remote_addr, request.method,
                    request.scheme, request.full_path)
    parametros_endpoint()
    if randint(0, 1) == 0:
        return http.client.BAD_REQUEST
    return render_template("lista.html", titulo="Fundo de Investimento Imobiliário")


@app.route('/criptos')
# @metrics.counter('efetivacao_criptos',
#                  'Número de papeis de criptos efetivados',
#                  labels={'tipo': 'CRIPTOS'})
def criptos():
    app.logger.info("%s %s %s %s", request.remote_addr, request.method,
                    request.scheme, request.full_path)
    parametros_endpoint()
    if randint(0, 1) == 0:
        return http.client.BAD_REQUEST
    return render_template("lista.html", titulo="Criptos")


if __name__ == "__main__":
    app.run(host="0.0.0.0")  # porta = 5000 -> http://127.0.0.1:5000/renda-fixa
    # app.run(host="0.0.0.0", port=5001)  # http://127.0.0.1:5001/renda-fixa
