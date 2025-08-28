# lambda/validation_lambda.py
import os
import urllib.request
import json

def handler(event, context):
    test_url = os.environ.get("TEST_URL")
    if not test_url:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "TEST_URL environment variable not set"})
        }
    try:
        with urllib.request.urlopen(test_url, timeout=10) as resp:
            body = resp.read().decode()
            status = resp.getcode()
            if status == 200 and "ok" in body.lower():
                return {
                    "statusCode": 200,
                    "body": json.dumps({"status": "validation passed"})
                }
            raise Exception(f"Unexpected response: {status} / {body}")
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"validation failed: {e}"})
        }
