{{/*
Expand the name of the chart.
*/}}
{{- define "api.fullname" -}}
{{- printf "%s-%s" .Release.Name "api" | trunc 63 | trimSuffix "-" -}}
{{- end -}}
