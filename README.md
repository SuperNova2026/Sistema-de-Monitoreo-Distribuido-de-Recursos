# Sistema de Monitoreo Distribuido de Recursos

Este proyecto permite monitorear el uso de recursos (CPU, memoria, disco, etc.) en múltiples computadoras conectadas en red utilizando herramientas como Prometheus y Grafana.

## Estructura del Proyecto

```
sistema-monitoreo-distribuido
├── src
│   ├── main.py                # Punto de entrada de la aplicación
│   ├── prometheus
│   │   └── prometheus.yml     # Configuración de Prometheus
│   ├── grafana
│   │   └── grafana.ini        # Configuración de Grafana
│   └── scripts
│       └── monitor.py         # Script para recopilar datos de recursos
├── requirements.txt           # Dependencias del proyecto
├── Dockerfile                  # Instrucciones para construir la imagen de Docker
└── README.md                   # Documentación del proyecto
```

## Requisitos

Asegúrate de tener instaladas las siguientes herramientas:

- Python 3.x
- Docker
- Prometheus
- Grafana

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd sistema-monitoreo-distribuido
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Configura Prometheus y Grafana editando los archivos `src/prometheus/prometheus.yml` y `src/grafana/grafana.ini` según tus necesidades.

## Uso

1. Ejecuta el script de monitoreo en cada computadora que deseas monitorear:
   ```
   python src/scripts/monitor.py
   ```

2. Inicia el servidor de monitoreo:
   ```
   python src/main.py
   ```

3. Inicia Prometheus y Grafana utilizando Docker:
   ```
   docker-compose up
   ```

4. Accede a la interfaz de Grafana en `http://localhost:3000` para visualizar las métricas.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.
