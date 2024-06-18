resource "aws_sqs_queue" "test_queue" {
  name = local.queue_name
}