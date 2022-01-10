#!/bin/bash
# Sends a GET request using a header variable and displays response body
curl -sH "X-School-User-Id:98" "$1"
