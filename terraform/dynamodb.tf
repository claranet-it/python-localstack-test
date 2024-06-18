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