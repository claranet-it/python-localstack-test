def write_to_queue_use_case(client, queue_name: str, data: str):
    client.send_message(
        QueueUrl=queue_name,
        MessageBody=data,
    )