from flask import Flask, jsonify
import psutil
import time
import threading

app = Flask(__name__)

def collect_metrics():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')

        metrics = {
            'cpu_usage': cpu_usage,
            'memory_usage': memory_info.percent,
            'disk_usage': disk_info.percent
        }

        # Here you would send the metrics to Prometheus
        # For example, using a push gateway or exposing an endpoint

        time.sleep(5)  # Adjust the sleep time as needed

@app.route('/metrics', methods=['GET'])
def metrics():
    # This endpoint would return the collected metrics in a format Prometheus can scrape
    return jsonify({
        'cpu_usage': psutil.cpu_percent(),
        'memory_usage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent
    })

if __name__ == '__main__':
    threading.Thread(target=collect_metrics, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)