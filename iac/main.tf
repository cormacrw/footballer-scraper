terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.63.0"
    }
  }
}

provider "aws" {
  # Configuration options
  region = "us-east-1"
}

resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = "football-data"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "fd_pk"
  range_key      = "fd_sk"

  attribute {
    name = "fd_pk"
    type = "S"
  }

  attribute {
    name = "fd_sk"
    type = "S"
  }

  ttl {
    attribute_name = "TimeToExist"
    enabled        = false
  }
}