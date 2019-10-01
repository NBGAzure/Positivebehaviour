import os

aws_access_key = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
aws_storage_bucket_name = os.environ.get('AWS_STORAGE_BUCKET_NAME')
SECRET_KEY = "2eef9ae2be10278a8b822199c834f15cff06915d5e56ec87"
DEBUG_VALUE = "True"


print(aws_access_key)
print(aws_secret_access_key)
print(aws_storage_bucket_name)