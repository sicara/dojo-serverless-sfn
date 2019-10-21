def handler(event, context):
    if not event["order"]["with_vegetables"]:
        return {}
    result = {
        "vegetables": {
            "carrots": True,
            "potatoes": False,
        },
    }
    return result
