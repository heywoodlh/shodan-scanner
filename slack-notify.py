#!/usr/bin/env python3
from slacker import Slacker
import sys
import subprocess
from auth import token, channel, enabled

slack = Slacker(token)

if enabled == "false":
    sys.exit(1)

f = open( "shodanhostscan.log")
messages = []
for line in f:
    messages.append(line)
f.close()

final_message = ''.join(messages)

message = print(final_message)

slack.chat.post_message(str(channel), str(message))
