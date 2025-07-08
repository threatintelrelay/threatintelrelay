#!/bin/bash
set -e
kubectl get namespace minio || kubectl create namespace minio
kubectl get namespace kong || kubectl create namespace kong
kubectl get namespace airflow || kubectl create namespace airflow
kubectl get namespace fastapi-app || kubectl create namespace fastapi-app
kubectl get namespace keycloak || kubectl create namespace keycloak