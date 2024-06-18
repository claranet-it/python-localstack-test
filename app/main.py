import json
import time

from config import BUCKET_NAME, TABLE_NAME, QUEUE_NAME

from infrastructure.s3_client import get_s3_client
from infrastructure.dynamodb_client import get_dynamodb_client
from infrastructure.sqs_client import get_sqs_client
from infrastructure.lambda_client import get_lambda_client

from use_case.read_from_bucket_use_case import read_from_bucket_use_case
from use_case.write_to_bucket_use_case import write_to_bucket_use_case
from use_case.write_to_dynamodb_use_case import write_to_dynamodb_use_case
from use_case.read_from_dynamodb_use_case import read_from_dynamodb_use_case
from use_case.write_to_queue_use_case import write_to_queue_use_case
from use_case.read_from_queue_use_case import read_from_queue_use_case
from use_case.list_functions_use_case import list_functions_use_case
from use_case.invoke_function_use_case import invoke_functions_use_case


s3_client = get_s3_client()
dynamodb_client = get_dynamodb_client()
sqs_client = get_sqs_client()
lambda_client = get_lambda_client()


def main(use_case):    
    match use_case:        
        case "1":
            with open('data/example.json', 'r') as f:
                data = f.read()
            
            write_to_bucket_use_case(
                s3_client, 
                bucket_name=BUCKET_NAME, 
                key="test-key", 
                data=data
            )
            print("Data written to bucket successfully")
        case "2":
            obj = read_from_bucket_use_case(
                s3_client, 
                bucket_name=BUCKET_NAME, 
                key="test-key"
            )
            data = json.loads(obj["Body"].read())
            print(data)        
        case "3":
            key = str(time.time())
            data = f"test-data {key}"
            write_to_dynamodb_use_case(
                dynamodb_client, 
                table_name=TABLE_NAME, 
                key=key, 
                data=data,
            )
            print("New item written to dynamodb - key: %s, data: %s" % (key, data))
        case "4":
            items = read_from_dynamodb_use_case(
                dynamodb_client, 
                table_name=TABLE_NAME,
            )
            print(items)        
        case "5":
            data = "{\"body\": \"test-data\"}"
            write_to_queue_use_case(
                sqs_client, 
                queue_name=QUEUE_NAME,
                data=data
            )
            print("New message written to SQS queue - data: %s" % (data))
        case "6":
            data = read_from_queue_use_case(
                sqs_client, 
                queue_name=QUEUE_NAME
            )
            if not "Messages" in data:
                print("No messages in the queue")
            else:
                print(data["Messages"][0]["Body"])
        case "7":
            functions = list_functions_use_case(lambda_client)
            print("\n".join([f"Function Name: {function['FunctionName']}, ARN: {function['FunctionArn']}" for function in functions]))
        case "8":
            response = invoke_functions_use_case(lambda_client)
            streaming_body = response['Payload']
            print(streaming_body.read().decode('utf-8'))
        case _:
            print("Invalid use case")
    


if __name__ == "__main__":
    prompt = """     
     1. Write to bucket
     2. Read from bucket     
     3. Write to DynamoDB
     4. Read from DynamoDB     
     5. Send message to SQS queue
     6. Read message from SQS queue
     7. List functions
     8. Invoke function

    Enter use case: 
    """
    
    use_case = input(prompt)
    main(use_case=use_case)

