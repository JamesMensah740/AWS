import boto3
import urllib.parse

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Extract bucket and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')
        
        print(f"File Content from {key}:")
        print(content)
        
        # You can extend this to write to DynamoDB or process data
        return {
            'statusCode': 200,
            'body': f"Successfully processed {key} from bucket {bucket}."
        }
    except Exception as e:
        print(f"Error processing object {key} from bucket {bucket}. Error: {str(e)}")
        raise e
