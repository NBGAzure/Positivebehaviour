import os

aws_access_key = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
aws_storage_bucket_name = os.environ.get('AWS_STORAGE_BUCKET_NAME')
print(aws_access_key)
print(aws_secret_access_key)
print(aws_storage_bucket_name)