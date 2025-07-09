---
title: Quickstart
description: Set up a local development environment for ThreatIntelRelay.
---
## Development Setup

The project relies on local Kubernetes with [Kind](https://kind.sigs.k8s.io/) and [Skaffold](https://skaffold.dev/) for iterative development.

### Prerequisites

- Docker
- `kubectl`
- `kind`
- `skaffold`
- `helm`

### Steps

1. Create a local Kubernetes cluster with the provided registry config:
   ```bash
   kind create cluster --config kind-config.yaml
   ```
2. Add convenient development domains to `/etc/hosts` (requires sudo):
   ```bash
   sudo deployment/scripts/dev-domains.sh add
   ```
3. Add Helm repositories and update them:
   ```bash
   ./deployment/scripts/add-helm-repos.sh
   ```
4. Create the required namespaces:
   ```bash
   ./deployment/scripts/create-namespaces.sh
   ```
5. Start Skaffold in dev mode to build and deploy the services:
   ```bash
   skaffold dev
   ```

When Skaffold completes, the FastAPI app is reachable at `https://api.localdev.me`.

---
This project is under active development; interfaces and infrastructure may change.
