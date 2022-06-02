import json
import logging
# import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Lambda2 Event: {}".format(event))
    logger.info("Function2 Name: {}".format(context.function_name))
    dummy1()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello From Function 2",
        }),
    }


def dummy1():
    logger.info("Dummy1!!!!")


def dummy2():
    logger.info("Dummy2!!!!")
