def handler(event, context):
    if not event["order"]["with_meat"]:
        return {}
    result = {
        "meat": {
            "steak": True,
            "sausage": False,
        },
    }
    return result
