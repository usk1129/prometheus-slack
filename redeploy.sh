#!/bin/bash
set -ex

kubectl delete deployment prometheus
kubectl apply -f deployment.yml
