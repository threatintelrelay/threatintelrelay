---
title: Stack Overview
description: Core components used by ThreatIntelRelay.
---

ThreatIntelRelay uses the following open-source tools:

- **Containers / Runtime**: Docker + Kubernetes
- **Scheduling / Event Flows**: Apache Airflow
- **Message Bus**: Apache Kafka
- **Immutable object store**: MinIO
- **Metadata DB**: PostgreSQL
- **Vector Index**: Qdrant
- **Enrichment / ETL**: Pydantic + pandas
- **Task / Queue manager**: Celery + Redis
- **API (with MCP endpoints)**: FastAPI
- **AuthN/AuthZ**: Keycloak
- **API gateway / rate-limit / WAF**: Kong Gateway + Modsecurity v3 with OWASP CRS 4
- **Edge caching**: Varnish Cache 6 + VCL
- **Observability**: OpenTelemetry -> Prometheus + Grafana + Loki + Tempo
- **CI/CD & supply chain**: GitHub Actions + Argo CD
- **Policy and runtime hardening**: Kyverno + Falco

This stack represents the planned architecture. ThreatIntelRelay is still being built, so expect changes as the MCP-based interface for AI agents takes shape.
