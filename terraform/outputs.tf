output "lambda_main_arn" {
  value = aws_lambda_function.lambda_main.arn
}

output "test_bucket_arn" {
  value = aws_s3_bucket.test_bucket.arn
}