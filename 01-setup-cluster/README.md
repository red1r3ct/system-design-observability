## Создание кластера

1. Собирать кластер будем на https://labs.play-with-k8s.com/. Заходим и регистрируемся
2. Нажимаем Add New Instance создаем 3 инстанса
3. На первой ноде инициализируем мастер ноду
    ```bash
    kubeadm init --apiserver-advertise-address $(hostname -i) --pod-network-cidr 10.5.0.0/16
    ```
    ```bash
    kubectl apply -f https://raw.githubusercontent.com/cloudnativelabs/kube-router/master/daemonset/kubeadm-kuberouter.yaml
    ```
4. Указываем путь до конфига для доступа через kubectl
    ```bash
    export KUBECONFIG=/etc/kubernetes/admin.conf
    ```
5. На других нодах вызываем команду для подключения к нодам (можно подсмотреть в выводе команды kubeadm init)
    ```bash
    kubeadm join 192.168.0.8:6443 --token <token> \
        --discovery-token-ca-cert-hash <hash>
    ```
    Опционально копируем /etc/kubernetes/admin.conf с node1 на другие машины и повторяем команду `export KUBECONFIG=/etc/kubernetes/admin.conf`
6. Проверим что ноды подключились
    ```bash
    kubectl get nodes
    ```
7. Устанавливаем service mesh Istio
    ```bash
    curl -L https://istio.io/downloadIstio | sh - && cd istio-1.19.3 && export PATH=$PWD/bin:$PATH && istioctl install --set profile=demo -y && kubectl label namespace default istio-injection=enabled
    ```
8. Устанавливаем тестовое приложение
    ```bash
    kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml
    ```
9. Запускаем ngrok чтобы открыть доступ к сервису. Это хак вместо L4 балансера так как playground не поддерживает такое.
    ```bash
    curl https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz > ngrok.tgz
    tar zxvf ngrok.tgz
    mv ngrok /bin/ngrok
    # copy ngrok.conf
    ngrok start --config ngrok.conf --all
    ```
