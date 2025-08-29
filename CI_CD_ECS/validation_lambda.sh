#!/bin/bash
set -e
# This script expects an environment variable TEST_URL set by your pipeline or CodeDeploy
if [ -z "$TEST_URL" ]; then
  echo "TEST_URL is not set. Exiting with failure."
  exit 1
fi

# simple curl test
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$TEST_URL")
if [ "$HTTP_CODE" -ge 200 ] && [ "$HTTP_CODE" -lt 400 ]; then
  echo "Validation success: $HTTP_CODE"
  exit 0
else
  echo "Validation failed: $HTTP_CODE"
  exit 2
fi
