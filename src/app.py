import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def handler(event, context):
    method = event['httpMethod']
    
    try:
        if method == 'POST':
            return create_item(json.loads(event['body']))
        elif method == 'GET':
            return get_item(event['pathParameters']['id'])
        elif method == 'PUT':
            return update_item(event['pathParameters']['id'], json.loads(event['body']))
        elif method == 'DELETE':
            return delete_item(event['pathParameters']['id'])
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}

def create_item(item):
    item_id = str(int(datetime.now().timestamp()))
    item['id'] = item_id
    table.put_item(Item=item)
    return {'statusCode': 201, 'body': json.dumps(item)}

def get_item(item_id):
    response = table.get_item(Key={'id': item_id})
    if 'Item' in response:
        return {'statusCode': 200, 'body': json.dumps(response['Item'])}
    return {'statusCode': 404, 'body': json.dumps({'message': 'Item not found'})}

def update_item(item_id, updates):
    table.update_item(
        Key={'id': item_id},
        UpdateExpression='SET #data = :data',
        ExpressionAttributeNames={'#data': 'data'},
        ExpressionAttributeValues={':data': updates.get('data')}
    )
    return {'statusCode': 200, 'body': json.dumps({'id': item_id, **updates})}

def delete_item(item_id):
    table.delete_item(Key={'id': item_id})
    return {'statusCode': 204, 'body': ''}
