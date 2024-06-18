locals {
  source_file   = "${path.module}/../app/lambda/main.py"
  output_path   = "${path.module}/../build/lambda_main.zip"
  function_name = "lambda_main-${var.stage}"
  bucket_name   = "test-bucket"
  queue_name    = "test-queue"  
}