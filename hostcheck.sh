#!/usr/bin/env bash
#Bash script for regularly checking on specific hosts to see if they have been scanned and posted on Shodan

GROUP="$(cat hosts.txt)"

shodan_scan() {
	DATE="$(date +%D\ %H:%M:%S)"
	echo "$DATE"
	echo "$HOSTNAME"
	./shodan host "$HOSTS"
	printf "\n"
	printf "\n"
}

HOSTNAME="$HOSTS"

for HOSTS in "$GROUP"
do
	if [[ "$HOSTS" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]] 
	then
	       shodan_scan >> shodanhostscan.log
	else
	       HOSTNAME="$HOSTS"
	       HOSTS=$(dig +short $HOSTS)
	       shodan_scan >> shodanhostscan.log
        fi	       
done
