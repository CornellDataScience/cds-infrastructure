#!/bin/sh

echo "This script will check to make sure you have a requirements.txt and will install using venv"

if ! command -v python3 -m venv  &> /dev/null
then
    echo "venv could not be found"
    exit
else
    echo "venv is installed!"
fi

