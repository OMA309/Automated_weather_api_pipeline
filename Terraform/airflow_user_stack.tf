resource "aws_s3_bucket" "botafli-weather-api" {
  bucket = "botafli-weather-api"

  tags = {
    Name        = "botafli-weather-api"
    Environment = "prod"
  }
}

resource "aws_s3_bucket" "tfstate_file_bucket" { # bucket for the tfstate credentials
  bucket = "botafli-backend-tfstate"

  tags = {
    Name        = "tfstate-credential"
    Environment = "prod"
  }
}


resource "aws_iam_user" "botafli-new-user" {
  name = "botafli-weather-user"
 

  tags = {
    tag-key = "botafli-new-user"
  }
}


resource "aws_iam_access_key" "botafli-access-key" {
  user = aws_iam_user.botafli-new-user.name
}


resource "aws_iam_user_policy" "botafli_policy" {
  name = "botafli-user-policy"
  user = aws_iam_user.botafli-new-user.name

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = [
          "s3:ListAllBuckets",
        ],
        Effect   = "Allow",
        Resource = "*"
      },
      {
        Action = [
          "s3:PutObject",
          "s3:DeleteObject",
        ],
        Effect   = "Allow",
        Resource = "arn:aws:s3:::botafli-weather-api/*"
      }
    ]
  })
}


