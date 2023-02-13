from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
app.debug = True
metrics = PrometheusMetrics(app)

@app.route('/')
def index():
    return '<h1>Home! Olá, mundo :)</h1>'

@app.route('/renda-fixa')
def renda_fixa():
    return render_template('lista.html', titulo='Renda fixa')

if __name__ == "__main__":
    # app.run(host="0.0.0.0")  # porta = 5000 -> http://127.0.0.1:5000/renda-fixa
    app.run(host="0.0.0.0", port=5001)  # http://127.0.0.1:5001/renda-fixa
