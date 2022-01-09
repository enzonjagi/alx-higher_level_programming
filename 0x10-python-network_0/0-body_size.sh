#!/usr/bin/env bash
# accepts a URL, sends a request to the URL and returns size of response body
curl "$1" -so /dev/null '%{size_download}\n'
