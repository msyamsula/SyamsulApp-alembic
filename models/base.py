from sqlalchemy.ext.declarative import declarative_base

# print(os.getenv("MYSQL_URI"), )
# engine = create_engine(url=os.getenv("MYSQL_URI"), echo=True, pool_size=20, max_overflow=0)
# metadata = MetaData()
Base = declarative_base()
# metadata = Base.metadata