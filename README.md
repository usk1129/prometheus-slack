## Prometheus-slack
Monitoring app with prometheus and send alert to slack channel with kubernetes cluster locally on minikube.
You can create your own docker image and push to docker hub or you can use my image.

My tree looks like this:
```
├── README.md
├── app
│   ├── Dockerfile
│   ├── deployment.yml
│   ├── hello.py
│   └── requirements.txt
├── configmap.sh
├── configs
│   ├── alertmanager.yml
│   ├── prometheus.yml
│   └── rules.yml
├── deployment.yml
├── permissions
│   └── permissions.yml
├── redeploy.sh
└── start_app.sh
```
## Start the project

Start the kubernetes cluster or local minikube cluster.

Deploy the falcon app image with:
```
$./start_app.sh
```
check the status of the pod with:
```
$kubectl get po -w
```
once its up run the following to open it in your browser:
```
$minikube service promsvr
```

Create the permissions from the yaml file that includes clusterRole, clusterRoleBinding, serviceAccount by running the command:
```
$cd permissions
$kubectl create -f permissions.yml
```
## Prometheus/Alertmanager Configs and Enhancing the Deployment Yaml

let's deploy our basic Prometheus deployment with their official image:
```
$kubectl create deployment prometheus --image=prom/prometheus

$kubectl expose deployment prometheus --type=NodePort --port=9090

$minikube service prometheus
```
In the menu, navigate to Status > Targets to see your Prometheus instance monitoring itself.

Replace ‘Extern_Service_url’ in the prometheus.yml file with the service url.
You can get it in the minikube cluster by running the command and include the output without HTTP://:

```
$minikube service promsvr  --url
```

Create slack channel or your existing channel and add incoming Webhooks to slack. To set this up check out this <a href="https://api.slack.com/messaging/webhooks" rev="en_rl_none" textcontent="link">link</a> and add Incoming Webhooks to slack. Once you have your webhook url add it to slack_api_url in alertmanager.yml

Create configmaps by running:
```
$./configmap.sh

```
Redeploy prometheus by running:
```
$./redeploy.sh
```
You should now have all of your services, pods, and configs in your minikube cluster. Let's try it out by bringing down our hello app.
```
$kubectl scale deployment prom-test --replicas=0
```
After the service is down for 1 minute, you should receive a critical alert for hello deployment in your slack channel. 
