import pandas 
from sqlalchemy import create_engine
import logging



def upload_to_rds(df,tablename,username,password,host,port,database):

    # Create the SQLAlchemy engine
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
    logging.info("connecting sqlalchemy to aws rds")
    logging.info("loading the data to rds")
    df.to_sql(tablename, con=engine, if_exists='replace', index=False)
    logging.info("loaded to rds")
