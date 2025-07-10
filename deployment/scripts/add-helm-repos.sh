#!/bin/bash
set -e

echo "Adding Kong Helm repo..."
helm repo add kong https://charts.konghq.com

echo "Adding Bitnami Helm repo..."
helm repo add bitnami https://charts.bitnami.com/bitnami || true

echo "Adding Airflow Helm repo..."
helm repo add airflow-stable https://airflow-helm.github.io/charts

echo "Adding Stable Helm repo..."
helm repo add stable https://charts.helm.sh/stable

echo "Adding MinIO Operator Helm repo..."
helm repo add minio-operator https://operator.min.io

echo "Adding Kyverno Helm repo..."
helm repo add kyverno https://kyverno.github.io/kyverno

echo "Updating all Helm repos..."
helm repo update

echo "All official Helm repositories have been added and updated!"
