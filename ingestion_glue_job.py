import sys
import time
import boto3
print("running job")
#time.sleep(6)
## Once the ETL completes
lambda_client = boto3.client('lambda')  ## Step-3
response = lambda_client.invoke(FunctionName='arn:aws:lambda:us-east-1:211631851183:function:lambdaToCreateEvent')  ## Step-4

