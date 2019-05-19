# COMPUTING & COGNITION
# ECHOBOT v0.2 Including MongoDB connection


import time
import random
# import the re module (regular expressions)
import re

responses = {
    "Hi":["Hello, how are you?","Hey,you again!", "How have you been?","Goodday, what's up?"],
    "How are you?":["I'm good, thanks for asking!"]
}

# define a function that checks for a certain pattern in the message
def check_pattern(message):
    pattern = "Do you remember"
    match = re.search(pattern, message)
    if match:
        return True

# If message not in responses, check for a pattern
def respond(message):
    if message in responses:
        return random.choice(responses[message])    
    elif check_pattern(message):
        return "I recognized a pattern."
    else:
        return "I didn't get that: {}".format(message)

def send_message(message):
    print("USER: {}".format(message))
    wait_time = random.randint(1,4)
    time.sleep(wait_time)    
    print("Echobot: {}".format(respond(message)))

while True:
    send_message(input())