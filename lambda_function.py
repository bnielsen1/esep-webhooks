import os
import json
import urllib.request
import urllib.parse

def lambda_handler(event, context):
    body = json.loads(event['body'])

    url = body['issue']['html_url']
    payload = 
    {
        "text": f"Issue Created: {url}"
    }
    
    payload_json = json.dumps(payload).encode('utf-8')
    webhook_url = os.environ['SLACK_URL']

    request = urllib.request.Request(webhook_url, data=payload_json, headers={'Content-Type': 'application/json'})
    response = urllib.request.urlopen(request)
    
    return {
        'statusCode': response.status,
        'body': response.read().decode('utf-8')
    }
