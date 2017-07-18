# shodan-scripts

## Description:
These scripts are intended to easily use Shodan's API to search and scan for hosts, vulnerabilities, etc. 

This collection of scripts are built on the Shodan Python module for the Shodan searches and the Slacker python module for Slack notification integration. 

These scripts were designed to use Slack as the main notification/logging agent. Without Slack integration there will not be a persistent text record of the log files if using the hostcheck.sh script.



#### File description:
- hostcheck.sh: Script that will search Shodan for any information posted on hosts specified in hosts.txt file and will send any relevant information to Slack channel specified in slack-notify.py (requires files shodan and slack-notify.py to be configured for Shodan/Slack integrations). This script uses the "shodan" file in this repository to do searches for the hosts using Shodan's API. It also uses the functionality of sqlite3 (built into the shodan program in this repository) to know which hosts to scan. Lastly, this script also uses slack-notify.py to send notifications to Slack using the API key and channel specified in slack-notify.py. See below for usage details.

- requirements.txt: Contains Python dependencies essential for scripts to run correctly.

- shodan: Python program that interacts with Shodan's API to search for key words or specific hosts. See below for usage information.

- shodanhostscan.log: Contains the information from the last scan performed by hostcheck.sh.

- slack-notify.py: Python program that will send the text in shodanhostscan.log to Slack. Contains token, channel and enabled variables which will need to be configured with correct information in order to send notifications.


## Usage:
First, install the dependencies in requirements.txt by running:

`sudo pip3 install -r requirements.txt`


#### Shodan Configuration
Edit "api_key" variable within shodan file to equal correct Shodan API key value.

#### Slack configuration
Edit "token" and "channel" variables within slack-notify.py to equal respective Slack API key (token) and Slack channel. Also change the 'enabled = "false"' to 'enabled = "true"' within slack-notify.py to enable Slack notifications.

The two files intended to be executed on their own is "shodan" and "hostcheck.sh". File "shodan" needs to be configured with Shodan API key or else it will not work.

### shodan
The shodan program is intended to search shodan for a keyword (such as webcams, apache, etc.) or for specific hosts. This program requires that you search hosts using IP addresses and not domain names.

- shodan usage example:
`./shodan search apache` -- this performs a keyword search on the word "apache"
`./shodan host 205.120.89.10`-- this performs a host lookup on Shodan for the IP address 205.120.89.10

The shodan program has been built with sqlite to store hostnames if continuous scanning is desired for specific hosts. These are the basic commands for this functionality:

`./shodan host-add 205.120.89.10` -- adds a host to be stored in sqlite database

`./shodan host-delete 205.120.89.10` -- deletes the host from the sqlite database

`./shodan host-list` -- lists all hosts stored in the database

`./shodan hostscan-all` -- performs a host scan on all hosts stored in the database

### hostcheck.sh
The hostcheck.sh script is intended to either be run as a cron job or as a stand alone script. Once it is executed it will read the hosts that have been added to the sqlite database through the shodan program in this repository and searches Shodan using the API to see if there is any relevant information specific to each respective host stored on Shodan. It will then save that output to shodanhostscan.log, overwriting any information that it may have stored previously. Then it executes slack-notify.py which reads the shodanhostscan.log file and sends that output to the respective Slack team and channel that is configured in slack-notify.py. 
