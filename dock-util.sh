#!/bin/bash


usage() {
	echo "Usage: $0 <COMMAND>" 1>&2
	echo "	update-image - update docker images" 1>&2
	echo "	clean-images - cleanup dangling (orphaned) docker images" 1>&2
	echo "	test - test command" 1>&2
	exit 1
}

clean_dangling_images() {
	echo "Cleaning dangling images.."
	docker rmi $(docker images -q --filter "dangling=true")
}

update_image() {
	echo "-----------------------------------------------------------"
	echo "Building ${1}..."
	cd ../$1
	git checkout master
	git status
	docker build -t mminderbinder/$1 .
	git checkout 0.9.15
	git status
	docker build -t mminderbinder/$1:0.9.15 .
	echo ""
}

update_images() {
	echo "Building latest docker images from mmminderbinder's repo..."
	for img in baseimage java-jdk7 tomcat7 apache2 gradle2 openam ; do
		update_image "${img}"
	done
	echo "done!"
}

if [[ -z "$1" ]]; then
	usage
fi

if [[ $1 == "update-image" ]]; then
	if [[ -n "$2" ]]; then
		echo "unsupported"
	else
		update_images
	fi
elif [[ $1 == "clean-images" ]]; then
	clean_dangling_images
elif [[ $1 == "test" ]]; then
	echo "Testing, testing, 1, 2, 3! Is this thing on?"
else
	usage
fi
