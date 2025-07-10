# Helm Charts Custom Values

In this directory, all custom configuration for Helm charts is managed through `<chartname>-values.yaml` files (for example, `airflow-values.yaml`, `fastapi-app-values.yaml`, etc.). The default `values.yaml` files provided by the official charts remain untouched.

When installing or upgrading a release, include your custom values file:

```bash
helm upgrade --install <release-name> <chart-name> -f <chartname>-values.yaml
```

This approach ensures that upstream `values.yaml` files are not altered, simplifying future chart upgrades and maintenance.
