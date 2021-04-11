#!/bin/bash
kubectl delete deployment prometheus
kubectl apply -f deployment.yml
