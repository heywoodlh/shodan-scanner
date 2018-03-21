# shodan-scanner

## Description:
`shodan_scanner` is intended to be a tool to more easily continuously monitor Shodan for relevant hosts using a local database for easier inventory.


#### File description:

- requirements.txt: Contains Python dependencies essential for scripts to run correctly.

- shodan_scanner: Python program that interacts with Shodan's API to search for key words or specific hosts. Stores specific hosts in database for scanning later. See below for usage information.


## Usage:
First, install the dependencies in requirements.txt by running:

`sudo pip3 install -r requirements.txt`


#### Shodan Configuration
Set the Shodan API key with this command: `./shodan_scanner init --api_key xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### shodan_scanner
The shodan program is intended to search shodan for hosts specifically.


There are two options for searching shodan: 


1. Perform a shodan search for a host using the `search` command.

2. Perform a direct host lookup using the `query` command.


In simplistic terms, the difference between `query` and `search` is that `query` will get specs and hard information whereas search is a little more flexible with the information it parses. 


- shodan_scanner usage example:

`./shodan search --host 63.55.55.55` -- this performs a keyword search on the word "apache"

`./shodan query --host 63.33.33.33`-- this performs a host lookup on Shodan for the IP address 205.120.89.10

The shodan program has been built with sqlite to store hostnames if continuous scanning is desired for specific hosts. These are the basic commands for this functionality:

`./shodan database --add 205.120.89.10` -- adds a host to be stored in sqlite database

`./shodan database --remove 205.120.89.10` -- deletes the host from the sqlite database

`./shodan database --list` -- lists all hosts stored in the database






##### shodan_scanner Query:

```
(shodan-scripts)❯ ./shodan_scanner query --help
usage: shodan_scanner query [-h] [--host HOST [HOST ...]] [--all] [--api KEY]
                            [--db FILE] [-q]

optional arguments:
  -h, --help            show this help message and exit
  --host HOST [HOST ...]
                        individual host(s)
  --all                 scan all hosts in local database
  --api KEY             shodan API key
  --db FILE             specify different local database file to utilize
  -q, --quiet           suppress output
```


##### shodan_scanner Search:

```
(shodan-scripts)❯ ./shodan_scanner search --help
usage: shodan_scanner search [-h] [--host HOST [HOST ...]] [--all] [--api KEY]
                             [--db FILE]

optional arguments:
  -h, --help            show this help message and exit
  --host HOST [HOST ...]
                        individual host(s)
  --all                 perform search on all hosts in local database
  --api KEY             shodan API key
  --db FILE             specify different local database file to utilize
```


##### shodan_scanner Database Manipulation:

```
(shodan-scripts)❯ ./shodan_scanner database --help
usage: shodan_scanner database [-h] [--add HOST [HOST ...]]
                               [--remove HOST [HOST ...]] [--list] [--db FILE]

optional arguments:
  -h, --help            show this help message and exit
  --add HOST [HOST ...]
                        host(s) to add to database
  --remove HOST [HOST ...]
                        host(s) to remove from database
  --list                list hosts in database
  --db FILE             specify different local database file to utilize
```
