import boto3

s3 = boto3.client('s3')
bucket_name = input("What bucket are you deleting from?  ")
file_name = input("What file are you deleting?  ")

s3.delete_object(Bucket=bucket_name, Key=file_name)

