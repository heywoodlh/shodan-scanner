#!/usr/bin/env bash
#Bash script for regularly checking on specific hosts to see if they have been scanned and posted on Shodan

#If you would like to enable slack notification please configure the slack variables in auth.py

AUTH_STATE="$(cat auth.py | grep "api_key")"
if [[ "$AUTH_STATE" == 'api_key = ""' ]]
then
	echo "please configure an api key in auth.py"
	exit 1
fi

GROUP="$(cat hosts.txt)"

shodan_scan() {
	DATE="$(date +%D\ %H:%M:%S)"
	echo "$DATE"
	echo "$HOSTNAME"
	./shodan host "$IND_HOSTS"
	printf "\n"
	printf "\n"
}

HOSTNAME="$HOSTS"

if [[ -f shodanhostscan.log ]]
then
	OLD_LOGS="$(cat shodanhostscan.log)"
	rm shodanhostscan.log
fi

for IND_HOSTS in "$GROUP"
do
	if [[ "$IND_HOSTS" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]] 
	then
		NEW_LOGS="$(shodan_scan)"
		if [[ "$NEW_LOGS" != "$OLD_LOGS" ]]
		then 
			NOTIFY="true"
		else
			NOTIFY="false" 
		fi

		echo "$NEW_LOGS" >> shodanhostscan.log
	else
	        HOSTNAME="$IND_HOSTS"
	        IND_HOSTS="$(dig +short $IND_HOSTS)"
		NEW_LOGS="$(shodan_scan)"

	        if [[ "$NEW_LOGS" != "$OLD_LOGS" ]]
	        then 
	       		NOTIFY="true"
	        else
			NOTIFY="false" 
	        fi

		echo "$NEW_LOGS" >> shodanhostscan.log
        fi	  	
done

slack_notifications() {
	./slack-notify.py
}

if [[ "$NOTIFY" == "true" ]] && [[ "$SLACK_API" != "" ]] && [[ "$CHANNEL" != "" ]] 
then
	slack_notifications
fi

