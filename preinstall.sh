#!/bin/bash

if [[ ! -z "$lalrochhara_ACCESS_TOKEN" ]]; then
    echo "Downloading lalrochhara_kit..."
    poetry run pip install git+https://${lalrochhara_ACCESS_TOKEN}@github.com/lalrochhara/lalrochhara_kit@v0.1.2
fi
