def write_to_bucket_use_case(client, bucket_name: str, key: str, data: str):
    client.put_object(
        Bucket=bucket_name, 
        Key=key, 
        Body=data
    )