1. Установите зависимости `pip install requirements.txt`
2. Запустите нагрузку `python3 load.py`
3. В графане можем посмотреть метрики например
    ```
    histogram_quantile(0.95, sum by(le) (rate(istio_request_duration_milliseconds_bucket{app="reviews"}[5m])))
    ```
4. Можно остановить ноду на который крутятся поды
    ```
    kubectl get pods --field-selector spec.nodeName=node1
    ```