import boto3

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id='AKIAVYAZAEJZG4RHKTXH',
    aws_secret_access_key='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'
)
for bucket in s3.buckets.all():
    bucket_name = bucket.name
    if '12921' in bucket_name:
        for obj in s3.Bucket(bucket_name).objects.all():
            splitted_key = obj.key.split('/')
            if splitted_key[1]:
                copy_source = {
                    'Bucket': 'siva-12921',
                    'Key': obj.key
                }
                s3.meta.client.copy(copy_source, 'siva-12900', obj.key)
                s3.Object("siva-12921", obj.key).delete()