cd configs && 
kubectl create configmap prometheus --from-file=prometheus.yml
kubectl create configmap alertmanager --from-file=alertmanager.yml
kubectl create configmap rules --from-file=rules.yml
