from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

import requests

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/')
def goodby_world():
    e = requests.get('http://service1:5001/')
    return f"Hello From Service 2, Service 1 says: {e.text}!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=False)
