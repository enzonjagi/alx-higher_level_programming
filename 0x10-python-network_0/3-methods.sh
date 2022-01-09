#!/usr/bin/env bash
# given a URL, this script displays all HTTP methods server will accept
curl -I "$1" -s | grep Allow | cut -d ' ' -f2-
