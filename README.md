# ThreatIntelRelay

A minimal FastAPI service deployed to Kubernetes with Helm and Skaffold. The service is exposed through a Kong Gateway ingress and is intended for local development with a [kind](https://kind.sigs.k8s.io/) cluster.

## Prerequisites

- Docker
- [kind](https://kind.sigs.k8s.io/)
- [Helm](https://helm.sh/)
- [Skaffold](https://skaffold.dev/)

## Getting started

### 1. Start a local Docker registry

```bash
docker run -d -p 5000:5000 --name kind-registry registry:2
```

### 2. Create the kind cluster

```bash
kind create cluster --config kind-config.yaml
```

### 3. Deploy with Skaffold

```bash
skaffold dev
```

Skaffold builds the API image, pushes it to the local registry and installs the Helm chart. It also port‑forwards the `threatintelrelay` service to `localhost:8000`. Access the FastAPI application at `http://localhost:8000`.

### 4. Install Kong (optional)

A Kong Gateway instance is required for the provided ingress rule. Install it with Helm:

```bash
helm repo add kong https://charts.konghq.com
helm repo update
helm install kong kong/kong --set ingressController.installCRDs=false
```

Port‑forward the proxy service if desired:

```bash
kubectl port-forward --namespace default service/kong-kong-proxy 8080:80
```

The API is then reachable at `http://localhost:8080/` via Kong.

### Cleanup

```bash
kind delete cluster
docker rm -f kind-registry
```
