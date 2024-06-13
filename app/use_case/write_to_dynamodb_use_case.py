def write_to_dynamodb_use_case(client, table_name: str, key: str, data: str):    
    client.put_item(
        TableName=table_name,
        Item={
            'id': {'S': key},
            'data': {'S': data}
        }
    )