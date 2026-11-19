FROM apache/superset:6.1.0-py312

USER root
RUN uv pip install --python /app/.venv/bin/python psycopg2-binary sqlalchemy-bigquery
USER superset
