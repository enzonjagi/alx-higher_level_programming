#!/usr/bin/env bash
# accepts a URL, sends a request to the URL and returns size of response body
curl "$1" -o /dev/null '%{size_download}\n' -s
