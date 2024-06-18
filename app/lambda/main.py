import json
import logging

def handler(event, context):    
    logging.info(f"Received event: {json.dumps(event)}")

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda OK!')
    }