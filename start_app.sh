#!/bin/bash
set -ex
cd app && kubectl apply -f deployment.yml
