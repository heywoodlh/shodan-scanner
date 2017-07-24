# shodan-scripts

## Description:
These scripts are intended to easily use Shodan's API to search and scan for hosts, vulnerabilities, etc. 

This collection of scripts are built on the Shodan Python module for the Shodan searches and the Slacker python module for Slack notification integration. 



#### File description:
- hostcheck.py: This program will scan all hosts specified in the shodan-scan database. It integrates with Slack and will send scan results to specified Slack channel.

- requirements.txt: Contains Python dependencies essential for scripts to run correctly.

- shodan_scanner: Python program that interacts with Shodan's API to search for key words or specific hosts. Stores specific hosts in database for scanning later. See below for usage information.

## Usage:
First, install the dependencies in requirements.txt by running:

`sudo pip3 install -r requirements.txt`


#### Shodan Configuration
Edit "api_key" variable within shodan file to equal correct Shodan API key value.

### shodan_scanner
The shodan program is intended to search shodan for a keyword (such as webcams, apache, etc.) or for specific hosts. This program requires that you search hosts using IP addresses and not domain names.

- shodan usage example:

`./shodan search apache` -- this performs a keyword search on the word "apache"

`./shodan host 205.120.89.10`-- this performs a host lookup on Shodan for the IP address 205.120.89.10

The shodan program has been built with sqlite to store hostnames if continuous scanning is desired for specific hosts. These are the basic commands for this functionality:

`./shodan host-add 205.120.89.10` -- adds a host to be stored in sqlite database

`./shodan host-delete 205.120.89.10` -- deletes the host from the sqlite database

`./shodan host-list` -- lists all hosts stored in the database

`./shodan hostscan-all` -- performs a host scan on all hosts stored in the database

### hostcheck.py
Hostcheck.py will scan all hosts that are in the shodan-scan database. Refer to the usage of shodan_scanner as to know how to list, add or remove hosts in database. In order for hostcheck.py to work the variable "shodan_api_key" will need to be set within hostcheck.py. 
This program was built with the intention of running as a scheduled, repeating job and then pushing the notifications to Slack.

#### Slack Configuration
In order to enable Slack integration to work properly, the variables "slack_token" and "slack_channel" will have to be set to the correct Slack API key and channel of the team the notifications will be sent to. In order to actually enable Slack notifications, the "slack_enabled" variable will have to be set to "true".
