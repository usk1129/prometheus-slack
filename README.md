# prometheus-slack
Monitoring app with prometheus and send alert to slack channel with kubernetes cluster

You can create your own docker image and push to docker hub or you can use my image. 

Start the kubernetes cluster or local minikube cluster.

Deploy the falcon app image with:

cd && kubectl create -f deployments.yml or run ./start_app.sh

check the status of the pod with:

kubectl get po -w

once its up run the following to open it in your browser:

minikube service promsvr

let's deploy our basic Prometheus deployment with their official image:

kubectl create deployment prometheus --image=prom/prometheus

kubectl expose deployment prometheus --type=NodePort --port=9090

minikube service prometheus

In the menu, navigate to Status > Targets to see your Prometheus instance monitoring itself.

Replace ‘Extern_Service_url’ in prometheus.yml file with the service url.

Create slack channel or your existing channel and add incoming Webhooks to slack. To set this up check out this link(https://api.slack.com/messaging/webhooks) and add Incoming Webhooks to slack. Once you have your webhook url add it to slack_api_url in alertmanager.yml

Create configmaps by running:

./configmap.sh

Redeploy prometheus by running:

./redeploy.sh

You should now have all of your services, pods, and configs in your minikube cluster. Let's try it out by bringing down our hello app.

kubectl scale deployment prom-test --replicas=0

After the service is down for 1 minute, you should receive a critical alert for hello deployment in your slack channel. 
