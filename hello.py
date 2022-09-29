#Copied from TA Alex: https://github.com/aianta/cgi-lab

#!/usr/bin/env python3

import os
import json

# Create an empty dictionary
env = {}

# Iterate through environment variables and add them to env
for env_key, env_value in os.environ.items():
    env[env_key] = env_value
    #print('{} -> {}'.format(env_key,env_value))

print("Content-Type: application/json")    # HTML is following
print()                             # blank line, end of headers

# Print env dictionary in json format
print(json.dumps(env))