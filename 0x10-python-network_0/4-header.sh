#!/usr/bin/env bash
# Sends a GET request using a header variable and displays response body
curl -H "X-School-User-Id:98" "$1" -s
