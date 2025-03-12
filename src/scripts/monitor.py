import psutil
import time
import requests

PROMETHEUS_PUSHGATEWAY_URL = 'http://<prometheus-pushgateway>:9091/metrics/job/resource_monitor'

def collect_metrics():
    cpu_usage = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    return {
        'cpu_usage': cpu_usage,
        'memory_usage': memory_info.percent,
        'disk_usage': disk_info.percent
    }

def push_metrics(metrics):
    data = f'cpu_usage {metrics["cpu_usage"]}\n'
    data += f'memory_usage {metrics["memory_usage"]}\n'
    data += f'disk_usage {metrics["disk_usage"]}\n'

    response = requests.post(PROMETHEUS_PUSHGATEWAY_URL, data=data)
    if response.status_code != 202:
        print(f'Failed to push metrics: {response.text}')

if __name__ == '__main__':
    while True:
        metrics = collect_metrics()
        push_metrics(metrics)
        time.sleep(10)