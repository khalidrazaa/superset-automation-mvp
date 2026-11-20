import os

from sqlalchemy.engine import URL

SECRET_KEY = os.environ["SUPERSET_SECRET_KEY"]
SQLALCHEMY_DATABASE_URI = URL.create(
    "postgresql+psycopg2",
    username=os.getenv("SUPERSET_DB_USER", "superset"),
    password=os.environ["POSTGRES_PASSWORD"],
    host=os.getenv("SUPERSET_DB_HOST", "postgres"),
    database=os.getenv("SUPERSET_DB_NAME", "superset"),
).render_as_string(hide_password=False)
