output "s3_bucket_name" {
  value = aws_s3_bucket.images.bucket
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.captions.name
}
