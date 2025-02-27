import os
import boto3 
import pandas as pd
import logging
from dotenv import load_dotenv
from Scripts.uploadtos3 import upload_folder_to_s3
from Scripts.downloadfroms3 import download_from_s3
from Scripts.csv_extract import extract_csv
from Scripts.xml_extract import extract_xml
from Scripts.json_extract import extract_json
from Scripts.transform import transform_df
from Scripts.load import load_csv
from Scripts.uploadto_rds import upload_to_rds


load_dotenv(dotenv_path='.env')

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY') #aws keys
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
HOST=os.getenv('HOST')

#s3Credentials
local_path='raw_data'
s3_path='dataset'
bucket_name='my-etl-project-bucket2'
folder_name='dataset/'
local_directory='dataset/'
output='output/'

#rdsCredentials
username = 'admin'
password = os.getenv('password')
host = HOST
port= 3306
database = 'guvi'
tablename="guvi_table"



def set_log():
    if not os.path.exists('logs'):
        os.makedirs('logs')
    with open('logs\\log.txt','a') as log_file:
        log_file.write('\n \n etl process with aws and python  \n')

    logging.basicConfig(
        filename='logs\\log.txt',  # Log file location
        level=logging.INFO,  
        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging

def main():
    set_log()
    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, \
                            aws_secret_access_key=AWS_SECRET_KEY,\
                            region_name='ap-south-1')
    logging.info("connected to s3")

    #local_path,bucket_name,s3_path
    upload_folder_to_s3(local_path,bucket_name,s3_path,s3_client)


    #bucket_name,folder_name,local_directory
    download_from_s3(bucket_name,folder_name,local_directory,s3_client)


    csv_df=extract_csv('raw_data')

    json_df=extract_json('raw_data')

    xml_df=extract_xml('raw_data')

    concat_df=pd.concat([csv_df,json_df,xml_df],ignore_index=True)

    transformed_df=transform_df(concat_df)

    load_csv(transformed_df,output)

    #df,username,password,host,port,database
    upload_to_rds(transformed_df,tablename,username,password,host,port,database)
    logging.info("process completed ")

if __name__=='__main__':
    main()
