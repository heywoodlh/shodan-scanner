#!/usr/bin/env python3
from slacker import Slacker
import sys
import subprocess

token = ""
channel = ""
enabled = "false"


slack = Slacker(str(token))

if enabled == "false":
    sys.exit(0)

f = open( "shodanhostscan.log")
messages = []
for line in f:
    messages.append(line)
f.close()

final_message = ''.join(messages)

slack.chat.post_message(str(channel), str(final_message))
