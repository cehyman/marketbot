from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

from config.config import Config
cfg = Config()

url = URL.create(
    drivername="postgresql",
    username=cfg.postgres_user,
    host=cfg.postgres_host,
    database=cfg.postgres_db,
    password=cfg.postgres_password,
    port=cfg.postgres_port,
)

engine = create_engine(url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


