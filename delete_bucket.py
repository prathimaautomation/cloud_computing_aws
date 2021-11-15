import boto3

s3 = boto3.client('s3')
bucket_name = input("What bucket are you deleting?  ")

s3.delete_bucket(Bucket=bucket_name)
