import config


def create_bucket_use_case(client, bucket_name: str):
    client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': config.AWS_REGION
        }
    )