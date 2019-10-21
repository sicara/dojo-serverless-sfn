import json
import os
import time

import boto3


def handler(event, context):
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    object_key = event["Records"][0]["s3"]["object"]["key"]
    sfn_input = {
        "bucket_name": bucket_name,
        "object_key": object_key,
    }
    sfn_client = boto3.client('stepfunctions')
    timestamp = int(1000 * time.time())
    execution_name = f'order-{timestamp}'
    sfn_client.start_execution(
        stateMachineArn=os.getenv("STATE_MACHINE_ARN"),
        name=execution_name,
        input=json.dumps(sfn_input),
    )
    body = {
        "message": "Launched stepfunction!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
