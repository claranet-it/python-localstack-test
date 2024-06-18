def create_queue_use_case(client, queue_name: str):
    client.create_queue(
        QueueName=queue_name
    )