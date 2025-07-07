{{/*
Expand the name of the chart.
*/}}
{{- define "api.fullname" -}}
{{- printf "%s-%s" .Release.Name "api" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Return the name of the api chart (for use in labels/selectors)
*/}}
{{- define "api.name" -}}
api
{{- end -}}
