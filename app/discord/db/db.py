import psycopg2

from marketbot.app.discord.config.config import Config
cfg = Config()

def connect():
   conn = psycopg2.connect(
      database=cfg.postgres_db, 
      user=cfg.postgres_user, 
      password=cfg.postgres_password, 
      host=cfg.postgres_host, 
      port= cfg.postgres_port
   )

   conn.close()

