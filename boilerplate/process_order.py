import json
import boto3


def handler(event, context):
    bucket_name = event["bucket_name"]
    object_key = event["object_key"]
    s3_client = boto3.client('s3')
    s3_response_object = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    object_content = s3_response_object['Body'].read()
    order = json.loads(object_content)

    return order
