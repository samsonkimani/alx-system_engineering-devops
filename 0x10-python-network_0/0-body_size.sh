#!/usr/bin/env bash
#check if there is an argument passed

if [ -z "$1" ]; then
	echo "Please provide a url for the argument"
	exit 1
fi

response=$(curl -s -o /dev/null -w "%{size_download}" $1)

echo "$response"
