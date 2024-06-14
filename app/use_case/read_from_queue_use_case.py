def read_from_queue_use_case(client, queue_name: str) -> str:
    return client.receive_message(
        QueueUrl=queue_name
    )