## Установка Prometheus

1. Устанавливаем Prometheus
    ```bash
    kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.19/samples/addons/prometheus.yaml
    ```
2. Устанавливаем Kiali. Kiali -- часть экосистемы Istio для визулизации взаимодействий в кластере
    ```bash
    kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.19/samples/addons/kiali.yaml
    ```
3. Добавляем ClusterIP сервиса kiali в ngrok
4. Устанавливаем Grafana
    ```bash
    kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.19/samples/addons/grafana.yaml
    ```
5. Добавляем ClusterIP сервиса grafana в ngrok