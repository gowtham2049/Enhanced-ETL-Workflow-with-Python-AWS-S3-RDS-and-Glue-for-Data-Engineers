import pandas as pd
import glob
import logging

def extract_json(path):
    logging.info("json reading")
    csv_file_list=glob.glob(f'{path}/*.json')
    df=[ pd.read_json(file,lines=True) for file in csv_file_list]
    concat_df=pd.concat(df)
    return concat_df