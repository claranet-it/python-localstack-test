def read_from_dynamodb_use_case(client, table_name: str) -> list:    
    response = client.scan(TableName=table_name)
    return response['Items']