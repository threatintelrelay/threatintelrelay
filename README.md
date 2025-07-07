# ThreatIntelRelay

This repository contains the ThreatIntelRelay microservice and Kubernetes deployment. The project is designed to be developed and tested locally with [kind](https://kind.sigs.k8s.io/), [skaffold](https://skaffold.dev/), and [helm](https://helm.sh/).

## Prerequisites

- Docker
- [kind](https://kind.sigs.k8s.io/)
- [skaffold](https://skaffold.dev/)
- [helm](https://helm.sh/)

Ensure these tools are installed and available in your PATH.

## Getting started

1. **Start a local registry**
   The cluster is configured to pull images from `localhost:5000`. Start a local registry:

   ```bash
   docker run -d --restart=always -p 5000:5000 --name kind-registry registry:2
   ```

2. **Create a kind cluster**

   ```bash
   kind create cluster --config kind-config.yaml --name threatintelrelay
   ```

   Connect the registry container to the cluster network:

   ```bash
   docker network connect kind kind-registry || true
   ```

3. **Build chart dependencies**

   ```bash
   helm dependency build deployment/helm/threatintelrelay
   ```

4. **Run the development loop**

   Use Skaffold to build images and deploy the helm chart:

   ```bash
   skaffold dev
   ```

   Skaffold watches the source code and automatically rebuilds and deploys on changes.

The API will be available through the Kong ingress controller once the chart is deployed.
