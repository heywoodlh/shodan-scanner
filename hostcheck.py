#!/usr/bin/env python3 
import os
import sys
from IPy import IP
import sqlite3
import dns.resolver
import shodan
from slacker import Slacker
import sys
import subprocess

slack_token = ""
slack_channel = ""
slack_enabled = "false"

shodan_api_key = ""

api_key = shodan_api_key

if api_key == str(""):
    print('please give api_key variable in ' + sys.argv[0] + ' the correct Shodan API value')
    sys.exit(0)

api = shodan.Shodan(api_key)

hostlist = []
conn = sqlite3.connect('shodan-scan')
c = conn.cursor()
try:
    c.execute('''CREATE TABLE hostnames
                (varchar)''')
except sqlite3.OperationalError:
    pass
for hosts in c.execute("SELECT * FROM hostnames"):
    domain_name = ''.join(hosts)
    hosts = domain_name
    try:
        IP(hosts)
        non_ip = 'false'
    except ValueError:
        def dig():
            for ip in dns.resolver.query(hosts, 'A'):
                return str(ip)
        hostlist.append(dig())
        non_ip = 'true'

if non_ip == 'true':
    hostnames = hostlist
info = []
for hosts in hostnames:
    host = api.host(hosts) 
    def gen_info():
        return ("IP: %s \n Organization: %s \n Operating System: %s" % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

    def other_info():
        for item in host['data']:
            return ("Port: %s \n Banner: %s \n" % (item['port'], item['data']))
    info.append(gen_info())
    info.append(other_info())


final_info = ''.join(info)

token = slack_token
channel = slack_channel
enabled = slack_enabled

slack = Slacker(str(token))

if enabled == "false":
    sys.exit(0)

slack.chat.post_message(str(channel), str(final_info))

