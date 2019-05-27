import time


def handle(event, context):
    print('Received %d records' % len(event['Records']))
    for record in event['Records']:

        # as we're using ttl to schedule executions, we do not care about inserts or updates,
        # only about removes which happen when the ttl is hit
        event_name = record['eventName']
        if event_name != 'REMOVE':
            print('Skipping %s' % event_name)
            continue

        # note that this image is in DynamoDB style, not a regular python object and needs to be converted accordingly
        item = record['dynamodb']
        old_image = item['OldImage']
        print(old_image['payload'])

        ttl = int(old_image['ttl']['N'])
        delay = int(time.time()) - ttl
        print('execution was %d seconds after ttl' % delay)
