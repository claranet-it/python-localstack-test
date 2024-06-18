resource "aws_s3_bucket" "test_bucket" {
  bucket = local.bucket_name
}