def read_from_bucket_use_case(client, bucket_name: str, key: str):
    try:
        return client.get_object(
            Bucket=bucket_name,
            Key=key
        )
    except Exception as e:
        return None
