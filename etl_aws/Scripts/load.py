import pandas as pd
import os
import logging
def load_csv(df,output):
    logging.info("loading the data to output folder")
    os.makedirs(output)
    df.to_csv(r'output\transformed_data.csv',index=False,mode='w')
