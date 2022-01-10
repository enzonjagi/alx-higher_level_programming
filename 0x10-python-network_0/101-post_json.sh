#!/bin/bash
# Sends POST request and displays body of the response
curl -i -X POST -H --data "$2" "Content-Type: application/json" -d "{\"key\":\"val\"}" "$1"
