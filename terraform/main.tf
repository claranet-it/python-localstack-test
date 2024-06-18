### Lambda function
resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

resource "aws_lambda_function" "lambda_main" {
  filename      = local.output_path
  function_name = local.function_name
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "main.handler"

  source_code_hash = data.archive_file.lambda.output_base64sha256

  runtime = "python3.12"
}

### S3 bucket and trigger
resource "aws_s3_bucket" "test_bucket" {
  bucket = local.bucket_name
}

resource "aws_s3_bucket_notification" "lambda_test_trigger" {
  bucket = aws_s3_bucket.test_bucket.id
  
  lambda_function {
    lambda_function_arn = aws_lambda_function.lambda_main.arn
    events              = ["s3:ObjectCreated:*"]
  }
}

### SQS queue
resource "aws_sqs_queue" "test_queue" {
  name = local.queue_name
}

### DynamoDB table
resource "aws_dynamodb_table" "test_table" {
  name      = local.table_name
  billing_mode = "PROVISIONED"
  read_capacity  = 5
  write_capacity = 5
  hash_key  = "id"

  attribute {
    name = "id"
    type = "S"
  }
}