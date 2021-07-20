from dotenv import load_dotenv, get_key
load_dotenv()
import configparser
import os


cfg = configparser.ConfigParser()
cfg.read("alembic.example.ini")

# uri
cfg["alembic"]["sqlalchemy.url"] = os.getenv("MYSQL_URI")
# timezone
cfg["alembic"]["timezone"] = os.getenv("TIMEZONE")

with open("alembic.ini", "w") as cfg_file:
    cfg.write(cfg_file)