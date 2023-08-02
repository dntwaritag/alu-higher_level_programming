#!/bin/bash
#Send request and get the size of the response body in bytes
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
