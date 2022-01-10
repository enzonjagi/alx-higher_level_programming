#!/bin/bash
# returns the status code of a HTTP response
curl -s -o /dev/null -I -w "%{http_code}" "$1"
