import boto3
import os
import logging

def upload_folder_to_s3(local_path,bucket_name,s3_path,s3_client):
    logging.info("uploading file to s3 bucket")
    for root,dirs,files in os.walk(local_path):
        
        for file_name in files:
            localpath=os.path.join(root,file_name)
            s3_file_path = os.path.join(s3_path, file_name).replace("\\", "/")  # Convert to proper S3 path format
            s3_client.upload_file(localpath,bucket_name, s3_file_path)