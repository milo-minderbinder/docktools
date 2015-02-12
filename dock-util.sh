#!/bin/bash


usage() {
	echo "Usage: $0 <COMMAND>" 1>&2
	echo "	clean-images	- cleanup dangling (orphaned) docker images" 1>&2
	echo "	test 		- test command" 1>&2
	exit 1
}

clean_dangling_images() {
	echo "Cleaning dangling images.."
	docker rmi $(docker images -q --filter "dangling=true")
}


if [[ -z "$1" ]]; then
	usage
fi

if [[ $1 == "clean-images" ]]; then
	clean_dangling_images
elif [[ $1 == "test" ]]; then
	echo "Testing, testing, 1, 2, 3! Is this thing on?"
else
	usage
fi
