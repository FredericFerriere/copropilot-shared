from sqlmodel import create_engine, Session
from sqlalchemy.engine import URL


def get_engine(host: str, port: int, dbname: str, user: str, password: str, sslmode: str = "require"):
    url = URL.create(
        "postgresql+psycopg2",
        username=user,
        password=password,
        host=host,
        port=port,
        database=dbname,
        query={"sslmode": sslmode},
    )
    return create_engine(url)
