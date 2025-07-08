---
title: Quickstart
description: Set up a local development environment for ThreatIntelRelay.
---

Follow these steps to run the project locally:

> **Note**: ThreatIntelRelay is a work in progress. The development environment may change frequently as features are added.

1. **Start a local registry**

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

```bash
skaffold dev
```

Skaffold watches the source code and automatically rebuilds and deploys on changes.

After the chart is deployed, the API will be available through the Kong ingress controller.
