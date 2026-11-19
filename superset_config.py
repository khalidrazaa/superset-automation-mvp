import os

from sqlalchemy.engine import URL

SECRET_KEY = os.environ["SUPERSET_SECRET_KEY"]
SQLALCHEMY_DATABASE_URI = URL.create(
    "postgresql+psycopg2",
    username="superset",
    password=os.environ["POSTGRES_PASSWORD"],
    host="postgres",
    database="superset",
).render_as_string(hide_password=False)
