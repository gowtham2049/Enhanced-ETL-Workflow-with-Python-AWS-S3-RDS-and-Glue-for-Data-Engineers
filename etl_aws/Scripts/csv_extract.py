import pandas as pd
import glob
import logging

def extract_csv(path):
    logging.info("csv reading")
    csv_file_list=glob.glob(f'{path}\*.csv')
    df = [pd.read_csv(file) for file in csv_file_list]  
    concat_df=pd.concat(df)
    return  concat_df       

