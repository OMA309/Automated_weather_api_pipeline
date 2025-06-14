resource "aws_ssm_parameter" "weather-accesskey" {
  name  = "/weather-api/weather-accesskey"
  type  = "SecureString"
  value = aws_iam_access_key.botafli-access-key.id
  description = "the access key for botafli-weather-user "
}

resource "aws_ssm_parameter" "weather-secretkey" {
  name  = "/weather-api/weather-secretkey"
  type  = "SecureString"
  value = aws_iam_access_key.botafli-access-key.secret
  description = "the secret key for botafli-weather-user "
}

