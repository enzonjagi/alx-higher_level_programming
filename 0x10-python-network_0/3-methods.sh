#!/bin/bash
# given a URL, this script displays all HTTP methods server will accept
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
