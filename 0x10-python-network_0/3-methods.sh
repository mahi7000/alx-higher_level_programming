#!/bin/bash
# display all HTTP methods the server will accept
curl -sX OPTIONS $1
