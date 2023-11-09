## Basic Virtual Service

Попробуем перенаправить все на ratings v1

1. Применяем destination-rules.yaml
    ```
    kubectl apply -f destination-rules.yaml
    ```
2. Применяем vs-all-v1.yaml в кластер. Все запросы пойдут только на reviews v1
    ```
    kubectl apply -f vs-all-v1.yaml
    ```
