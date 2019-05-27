import boto3
import time
from uuid import uuid4


# keep the db initialization outside of the functions to maintain them as long as the container lives
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
scheduling_table = dynamodb.Table('lambda-scheduling')


def delay():
    return 10


def handle(payload, context):
    print(payload)
    id = str(uuid4())
    ttl = int(time.time()) + delay()
    item = {
        'id': id,
        'ttl': ttl,
        'payload': payload
    }
    scheduling_table.put_item(Item=item)
