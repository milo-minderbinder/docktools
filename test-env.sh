#!/bin/bash

ORIG_HOSTS=./orig_hosts
MOD_HOSTS=./mod_hosts

usage() {
	echo "Usage: $0 <up|down>" 1>&2
	echo "	up - set up the OpenAM test environment" 1>&2
	echo "	down - tear down the OpenAM test environment" 1>&2
	exit 1
}

set_up() {
	cp /etc/hosts $ORIG_HOSTS
	cp $MOD_HOSTS /etc/hosts
	if [[ $1 == "-P" ]]; then
		docker run -d -P --name openam -h openam.example.com mminderbinder/openam:configured
		echo "Press enter when OpenAM server is up, to continue with Web Agent installation..."
		read enter_press
		docker run -d -P --name apache -h www.example.com --link=openam:openam.example.com mminderbinder/example-apache2
	else
		docker run -d -p 8080:8080 --name openam -h openam.example.com mminderbinder/openam:configured
		echo "Press enter when OpenAM server is up, to continue with Web Agent installation..."
		read enter_press
		docker run -d -p 80:80 --name apache -h www.example.com --link=openam:openam.example.com mminderbinder/example-apache2
	fi
	echo "done set up!"
}

tear_down() {
	cp $ORIG_HOSTS /etc/hosts
	echo "restored hosts file!"
	docker stop openam
	docker rm openam
	docker stop apache
	docker rm apache
	echo "done tear down!"
}

if [[ "$EUID" -ne "0" ]]; then
	echo "Must run $0 as root!"
	exit 1
fi

if [[ -z "$1" ]]; then
	usage
fi

if [[ $1 == "up" ]]; then
	if [[ -n "$2" ]]; then
		set_up "$2"
	else
		set_up
	fi
elif [[ $1 == "down" ]]; then
	tear_down
else
	usage
fi
