import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # TODO implement
    print(event)
    client= boto3.client('events')
#     response = client.create_event_bus(
#     Name='travel_data_by_code',
#     Tags=[
#         {
#             'Key': 'sealid',
#             'Value': '110397'
#         },
#     ]
# )
    
#     response = client.put_rule(
#     Name='Event_rule_by_code',
#     EventPattern='{"detail": {\
#     "source": ["orxe", "maui"],\
#     "object": ["orders", "transactions"]\
#   }}'
# ,
#     State='ENABLED',
#     Description='Event_rule_by_code',
#     #,RoleArn='string',
#     Tags=[
#         {
#             'Key': 'sealid',
#             'Value': '110397'
#         },
#     ],
#     EventBusName='traveleventbus'
# )
    response = client.put_events(
    Entries=[{
            'Time': datetime(2015, 1, 1),
            'Source': 'orxe',
            'Resources': [],
            'DetailType': "test_send_events",
            'Detail': json.dumps(event),
            'EventBusName': "arn:aws:events:us-east-1:211631851183:event-bus/traveleventbus"
        },
    ]
)
    return response
    # {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
