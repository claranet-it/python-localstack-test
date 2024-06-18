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