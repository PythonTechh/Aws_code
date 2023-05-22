
import json
import urllib.parse
import boto3
import csv
import io

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print(event)
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print("bucket", bucket, "key", key )
    #print(s3.list_objects(Bucket='travel101'))
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        #return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

    print("response", response)
    #Process it
    data = response['Body'].read().decode('utf-8')
    print("Data *****", data)
    reader = csv.reader(io.StringIO(data))
    #next(reader)
    #for row in reader:
        # print(str.format("Year - {}, Level - {}, Name - {}", row[0], row[1], row[2]))