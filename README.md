# Threat Intel Relay

The Threat Intel Relay aims to expose multiple open-source threat feeds over a Model Context Protocol (MCP) API. The stack below illustrates the overall scheme. **This repository is a work in progress and many components are still experimental.**

## Architecture

- **Containers/Runtime:** Docker and Kubernetes
- **Scheduling & Event Flow:** Apache Airflow
- **Message Bus:** Apache Kafka
- **Object Storage:** MinIO
- **Metadata Database:** PostgreSQL
- **Vector Index:** Qdrant
- **ETL/Enrichment:** Pydantic and pandas
- **Task & Queue Manager:** Celery with Redis
- **API & MCP Endpoints:** FastAPI
- **Authentication & Authorization:** Keycloak
- **Gateway / Rate Limiting / WAF:** Kong Gateway with ModSecurity v3 and OWASP CRS 4
- **Edge Caching:** Varnish Cache 6 with VCL
- **Observability:** OpenTelemetry exporting to Prometheus, Grafana, Loki and Tempo
- **CI/CD & Supply Chain:** GitHub Actions with Argo CD
- **Policy & Runtime Hardening:** Kyverno and Falco

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
