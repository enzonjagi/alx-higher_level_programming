#!/usr/bin/env bash
# accepts a URL, sends a GET request to the URL and returns the response body
curl -L "$1" -s