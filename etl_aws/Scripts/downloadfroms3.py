import boto3
import os
import logging

def download_from_s3(bucket_name,folder_name,local_directory,s3_client):
    logging.info("downloading dataset from s3")
    if not os.path.exists(local_directory):
        os.makedirs(local_directory)

    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)

    if 'Contents' in response:
        for obj in response['Contents']:
            file_key = obj['Key']
            file_name = file_key.split('/')[-1]  # Get the file name from the full path
        
            local_file_path = os.path.join(local_directory, file_name)

            s3_client.download_file(bucket_name, file_key, local_file_path)
        logging.info("loading data to dataset folder")
    else:
        print("No files found in the specified folder.")
