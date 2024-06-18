import boto3
import config


def get_lambda_client():
    if config.USE_LOCAL_INFRA:
        return boto3.client(
            "lambda",
            endpoint_url=config.AWS_ENDPOINT_URL,
            aws_access_key_id="test",
            aws_secret_access_key="test",
            region_name=config.AWS_REGION,       
        )
    return boto3.client("lambda")
