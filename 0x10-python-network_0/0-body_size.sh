#!/bin/bash
# accepts a URL, sends a request to the URL and returns size of response body
curl "$1" -sI | awk '/Content-Length/ { print $2 }'
