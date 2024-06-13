import json
import time
from infrastructure.s3_client import get_s3_client
from infrastructure.dynamodb_client import get_dynamodb_client
from use_case.read_from_bucket_use_case import read_from_bucket_use_case
from use_case.write_to_bucket_use_case import write_to_bucket_use_case
from use_case.create_bucket_use_case import create_bucket_use_case
from use_case.create_dynamodb_table import create_dynamodb_table
from use_case.write_to_dynamodb_use_case import write_to_dynamodb_use_case
from use_case.read_from_dynamodb_use_case import read_from_dynamodb_use_case


BUCKET_NAME = "test-bucket"
TABLE_NAME = "test-table"

s3_client = get_s3_client()
dynamodb_client = get_dynamodb_client()


def main(use_case):    
    match use_case:
        case "1":
            create_bucket_use_case(
                s3_client, 
                bucket_name=BUCKET_NAME
            )
            print("Bucket created successfully")        
        case "2":
            with open('data/example.json', 'r') as f:
                data = f.read()
            
            write_to_bucket_use_case(
                s3_client, 
                bucket_name=BUCKET_NAME, 
                key="test-key", 
                data=data
            )
            print("Data written to bucket successfully")
        case "3":
            obj = read_from_bucket_use_case(
                s3_client, 
                bucket_name=BUCKET_NAME, 
                key="test-key"
            )
            data = json.loads(obj["Body"].read())
            print(data)
        case "4":
            create_dynamodb_table(
                dynamodb_client, 
                table_name=TABLE_NAME, 
            )
            print("Table created successfully")
        case "5":
            key = str(time.time())
            data = f"test-data {key}"
            write_to_dynamodb_use_case(
                dynamodb_client, 
                table_name=TABLE_NAME, 
                key=key, 
                data=data,
            )
            print("New item written to dynamodb - key: %s, data: %s" % (key, data))
        case "6":
            items = read_from_dynamodb_use_case(
                dynamodb_client, 
                table_name=TABLE_NAME,
            )
            print(items)
        case _:
            print("Invalid use case")
    


if __name__ == "__main__":
    prompt = """
    1. Create bucket
    2. Write to bucket
    3. Read from bucket
    4. Create DynamoDB table
    5. Write to DynamoDB
    6. Read from DynamoDB

    Enter use case: 
    """
    
    use_case = input(prompt)
    main(use_case=use_case)

