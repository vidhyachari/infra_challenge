import boto3
from botocore.client import Config
import sys
from datetime import datetime

#######
## Sccript to cleanup old Deployments
##
#######

s3 = boto3.client('s3', endpoint_url='http://localhost:4566', config=Config(signature_version='s3v4')) # Use LocalStack endpoint

BUCKET_NAME = 's3-vidhya-test'

def sort_by_value(item):
    return item[1]

def main(dry_run=False):
    # Read X from command line arg
    if len(sys.argv) < 2:
        sys.exit(1)
    deployments_to_keep = int(sys.argv[1])

    # Get a list of all deployment folders
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    # Create a dict object to store the creation dates of each deployment folder
    folders = {}
    for obj in response['Contents']:
        if obj['Key'].endswith('/'):
            folders[obj['Key']] = obj['LastModified']

    # Sort the dictionary by creation date
    sorted_folders = sorted(folders.items(), key=sort_by_value, reverse=True)

    # iterate through sorted_folders starting from the index deployments_to_keep until the end
    for folder in sorted_folders[deployments_to_keep:]:
        folder_name, _ = folder
        print(f"Deleting {folder_name}")
        if not dry_run:
            response = s3.delete_object(Bucket=BUCKET_NAME, Key=folder_name)
           

if __name__ == '__main__':
    if '--dry-run' in sys.argv:
        main(dry_run=True)
    else:
        main()