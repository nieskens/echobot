# COMPUTING & COGNITION
# ECHOBOT v0.2 

import time
import random
import re

responses = {
    "Hi":["Hello, how are you?","Hey,you again!", "How have you been?","Goodday, what's up?"],
    "How are you?":["I'm good, thanks for asking!"]
}

# Adding parentheses in the pattern string defines a group. 
def check_pattern(message):
    pattern = "Do you remember (.*)"
    match = re.search(pattern, message)
    if match:
        # return the substring without the pattern
        return match.group(1)

def respond(message):
    if message in responses:
        return random.choice(  responses[message]  )    
    elif check_pattern(message):
        return "Of course I remember {}".format(check_pattern(message))
    else:
        return "I didn't get that: {}".format(message)

def send_message(message):
    print("USER: {}".format(message))
    wait_time = random.randint(1,4)
    time.sleep(wait_time)    
    print("Echobot: {}".format(respond(message)))

while True:
    send_message(input())