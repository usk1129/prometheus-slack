#!/bin/bash
kubectl delete deployment prometheus
kubectl create -f deployment.yml
