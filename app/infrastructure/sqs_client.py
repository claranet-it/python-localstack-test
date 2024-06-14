import boto3
import config


def get_sqs_client():
    if config.USE_LOCAL_INFRA:
        return boto3.client(
            "sqs",
            endpoint_url=config.AWS_ENDPOINT_URL,
            aws_access_key_id="test",
            aws_secret_access_key="test",            
        )
    return boto3.client("sqs")
