import boto3
import json
import logging
import time

logger = logging.getLogger("handler_logger")
logger.setLevel(logging.DEBUG)

dynamodb = boto3.resource("dynamodb")

DYNAMODB_TABLE_NAME = "serverless-github-collector-table"


def _get_response(status_code, body):
    if not isinstance(body, str):
        body = json.dumps(body)
    return {"statusCode": status_code, "body": body}


def analyze(event, context):
    logger.info("analyze requested.")

    table = dynamodb.Table(DYNAMODB_TABLE_NAME)
    timestamp = int(time.time())
    logger.info(str(timestamp))
    connectionID = context.aws_request_id

    item = {
        "connectionID": connectionID,
        "repository": "TIL",
        "Index": 0,
        "Timestamp": timestamp,
        "Username": "shinkeonkim",
        "Content": "PING!",
    }

    logger.info(str(item))

    table.put_item(Item=item)

    logger.info("Item added to database.")

    return _get_response(200, "Success")
