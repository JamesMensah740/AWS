import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'YourDynamoDBTable')  # Set via Lambda environment variable
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    print("Received event:", json.dumps(event, indent=2))

    s3 = boto3.client('s3')

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        try:
            response = s3.get_object(Bucket=bucket, Key=key)
            data = json.loads(response['Body'].read())

            # If data is a list of items
            if isinstance(data, list):
                for item in data:
                    table.put_item(Item=item)
            # If it's a single item (dictionary)
            elif isinstance(data, dict):
                table.put_item(Item=data)
            else:
                print("Unsupported JSON format")

            print(f"Data from {key} inserted into {table_name}")

        except Exception as e:
            print(f"Error processing file {key}: {str(e)}")

    return {"statusCode": 200, "body": "Processing complete"}
