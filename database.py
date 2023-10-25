from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib

SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://sa:314159265@B20DCCN728/PTHTTM_N11?driver=ODBC+Driver+17+for+SQL+Server"
#mssql+pyodbc://your_username:your_password@server_name/database_name?driver=ODBC+Driver+17+for+SQL+Server
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    # ,
    # connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()