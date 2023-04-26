import requests
import boto3
from botocore.client import Config

######
##Create Bucket and folders
#######

# Set the endpoint URL for localstack
s3 = boto3.client('s3', endpoint_url='http://localhost:4566', config=Config(signature_version='s3v4'))

# Create a new bucket
bucket_name = 's3-vidhya-test'
s3.create_bucket(Bucket=bucket_name)

# Create a folder inside the bucket
folder_name = 'deployhash112/'
s3.put_object(Bucket=bucket_name, Key=(folder_name))

# Create a file inside the folder
file_name = 'index.html'
file_content = '<html><body><h1>Hello World!</h1></body></html>'
s3.put_object(Bucket=bucket_name, Key=(folder_name + file_name), Body=file_content, ContentType='text/html')

# Create a folder inside the bucket
folder_name = 'dsfsfsl9074/'
s3.put_object(Bucket=bucket_name, Key=(folder_name))

# Create a file inside the folder
file_name = 'index.html'
file_content = '<html><body><h1>Hello World!</h1></body></html>'
s3.put_object(Bucket=bucket_name, Key=(folder_name + file_name), Body=file_content, ContentType='text/html')


# Create a folder inside the bucket
folder_name = 'delkjlkploy3/'
s3.put_object(Bucket=bucket_name, Key=(folder_name))

# Create a file inside the folder
file_name = 'index.html'
file_content = '<html><body><h1>Hello World!</h1></body></html>'
s3.put_object(Bucket=bucket_name, Key=(folder_name + file_name), Body=file_content, ContentType='text/html')


folder_name = 'dsfff1234321/'
s3.put_object(Bucket=bucket_name, Key=(folder_name))

# Create a file inside the folder
file_name = 'index.html'
file_content = '<html><body><h1>Hello World!</h1></body></html>'
s3.put_object(Bucket=bucket_name, Key=(folder_name + file_name), Body=file_content, ContentType='text/html')

folder_name = 'klljkjkl123/'
s3.put_object(Bucket=bucket_name, Key=(folder_name))

# Create a file inside the folder
file_name = 'index.html'
file_content = '<html><body><h1>Hello World!</h1></body></html>'
s3.put_object(Bucket=bucket_name, Key=(folder_name + file_name), Body=file_content, ContentType='text/html')
