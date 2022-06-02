import json
import logging
# import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Lambda Event: {}".format(event))
    logger.info("Function Name: {}".format(context.function_name))
    dummy1()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }


def dummy1():
    logger.info("Dummy1!!!!")


def dummy2():
    logger.info("Dummy2!!!!")
