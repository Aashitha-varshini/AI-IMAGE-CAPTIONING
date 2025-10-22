provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "images" {
  bucket = var.s3_bucket_name
}

resource "aws_dynamodb_table" "captions" {
  name         = var.dynamodb_table_name
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "user_id"
  range_key    = "image_id"

  attribute {
    name = "user_id"
    type = "S"
  }
  attribute {
    name = "image_id"
    type = "S"
  }
}

variable "aws_region" {
  default = "us-east-1"
}

variable "s3_bucket_name" {
  default = "your-s3-bucket"
}

variable "dynamodb_table_name" {
  default = "your-dynamodb-table"
}
