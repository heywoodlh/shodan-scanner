#!/usr/bin/env python3
from slacker import Slacker
import sys
import subprocess
from auth import token, channel, enabled

slack = Slacker(str(token))

if enabled == "false":
    sys.exit(1)

f = open( "shodanhostscan.log")
messages = []
for line in f:
    messages.append(line)
f.close()

final_message = ''.join(messages)

slack.chat.post_message(str(channel), str(final_message))
