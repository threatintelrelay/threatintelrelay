FROM apache/airflow:2.8.4-python3.9

# install your DAGs' dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt && pip install --no-cache-dir apache-airflow-providers-postgres psycopg2-binary

# copy DAGs & plugins into the image
COPY ./dags /opt/airflow/dags
# COPY ./plugins /opt/airflow/plugins

# (optional) add entrypoint hooks, healthchecks, etc.
