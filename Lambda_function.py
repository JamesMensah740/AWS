import boto3
import json

s3 = boto3.client('s3')
lambda_client = boto3.client('lambda')

bucket_name = 'your-bucket-name'
lambda_function_arn = 'arn:aws:lambda:us-east-1:123456789012:function:your-function-name'

# Add permission to allow S3 to invoke Lambda
lambda_client.add_permission(
    FunctionName='your-function-name',
    StatementId='s3invoke',
    Action='lambda:InvokeFunction',
    Principal='s3.amazonaws.com',
    SourceArn=f'arn:aws:s3:::{bucket_name}',
)

# Configure the notification
notification_configuration = {
    'LambdaFunctionConfigurations': [
        {
            'LambdaFunctionArn': lambda_function_arn,
            'Events': ['s3:ObjectCreated:*'],
        }
    ]
}

response = s3.put_bucket_notification_configuration(
    Bucket=bucket_name,
    NotificationConfiguration=notification_configuration
)

print("S3 Trigger configured:", response)
# This code configures an S3 bucket to trigger a Lambda function when an object is created in the bucket.