#!/usr/bin/env bash
# takes in a URL, sends a POST req to the passed URL, and displays the resp body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"