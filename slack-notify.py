#!/usr/bin/env python3
from slacker import Slacker
import sys

token = sys.argv[1]
channel = sys.argv[2]
message = sys.argv[3]

slack = Slacker('token')

# replace '#general' with correct slack channel and 'Hello fellow slackers!' with your message
    slack.chat.post_message(str(token), str(message))
