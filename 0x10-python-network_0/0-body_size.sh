#!/bin/bash
# takes in a URL and sends a request and display size of body

curl -s $1 | wc -c
