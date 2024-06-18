provider "aws" {
  region = var.region
}

terraform {
  required_providers {
    aws = {
      version = ">= 5.5.0"
      source  = "hashicorp/aws"
    }
  }

  required_version = "~> 1.0"
}
