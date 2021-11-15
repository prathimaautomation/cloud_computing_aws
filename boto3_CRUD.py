import boto3
import logging
from botocore.exceptions import ClientError
import os

def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def empty_bucket(bucket_name):
    """empty an s3 bucket"""
    s3 = boto3.client('s3')
    bucket_name = input("What bucket are you deleting?  ")
    s3.delete_bucket(Bucket=bucket_name)


s3 = boto3.client('s3')
bucket_name = input("What bucket are you downloading from?  ")
object_name = input("What is the object name to download?  ")
local_name = input("Choose a name for the local file download:  ")



s3.download_file(bucket_name, object_name, local_name)

bucket_name = input("Enter the bucket name:  ")
bucket_region = input("Enter the region for the bucket:  ")
create_bucket(bucket_name, bucket_region)