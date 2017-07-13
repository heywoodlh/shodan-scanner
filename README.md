# shodan-scripts

## Description:
These scripts are intended to easily use Shodan's API to search and scan for hosts, vulnerabilities, etc. 

This collection of scripts are built on the Shodan Python module for the Shodan searches and the Slacker python module for Slack notification integration. 

These scripts were designed to use Slack as the main notification/logging agent. Without Slack integration there will not be a persistent text record of the log files if using the hostcheck.sh script.



#### File description:
- auth.py: Contains configuration information for Shodan's API key and Slack's API key and channel information. All scripts depend on this file being configured correctly in order to work.

- hostcheck.sh: Script that will search Shodan for any information posted on hosts specified in hosts.txt file and will send any relevant information to Slack channel specified in auth.py (requires auth.py to be configured for Shodan/Slack integrations). This script uses the "shodan" file in this repository to do searches for the hosts using Shodan's API. It also uses hosts.txt to know which hosts to scan. Lastly, this script also uses slack-notify.py to send notifications to Slack using the API key and channel specified in auth.pyi. See below for usage details.  

- hosts.txt: File that contains desired hosts for hostcheck.sh. IP addresses or hostnames are compatible but will need to be separated line by line in order for the hostcheck.sh script to parse it correctly.

- requirements.txt: Contains Python dependencies essential for scripts to run correctly.

- shodan: Python program that interacts with Shodan's API to search for key words or specific hosts. See below for usage information.

- shodanhostscan.log: Contains the information from the last scan performed by hostcheck.sh.

- slack-notify.py: Python program that will send the text in shodanhostscan.log to Slack. Requires auth.py to be configured with the Slack API key and channel in order to work correctly.



## Usage:
First, install the dependencies in requirements.txt by running:

`sudo pip3 install -r requirements.txt`


The two files intended to be executed on their own is "shodan" and "hostcheck.sh". Both require auth.py to be configured before they can be used.

#### shodan
The shodan program is intended to search shodan for a keyword (such as webcams, apache, etc.) or for specific hosts. This program requires that you search hosts using IP addresses and not domain names.

- shodan usage example:
`./shodan search apache` 
`./shodan host 205.120.89.10`

#### hostcheck.sh
The hostcheck.sh script is intended to either be run as a cron job or as a stand alone script. Once it is executed it will read the hosts.txt file and search Shodan using the API to see if there is any relevant information specific to that host stored on Shodan. It will then save that output to shodanhostscan.log, overwriting any information that it may have stored previously. Then it executes slack-notify.py which reads the shodanhostscan.log file and sends that output to the respective Slack team and channel that is configured in auth.py. 
