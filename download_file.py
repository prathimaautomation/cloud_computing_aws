import boto3

s3 = boto3.client('s3')
bucket_name = input("What bucket are you downloading from?  ")
object_name = input("What is the object name to download?  ")
local_name = input("Choose a name for the local file download:  ")


s3.download_file(bucket_name, object_name, local_name)
