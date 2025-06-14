terraform {
  backend "s3" {
    bucket = "botafli-backend-tfstate"
    key = "weather_api/Terraform/terraform.tfstate"
    region = "us-east-2"
  }
}