# COMPUTING & COGNITION
# ECHOBOT v0.2 
import time
import random
import re

responses = {
    "Hi":["Hello, how are you?","Hey,you again!", "How have you been?","Goodday, what's up?"],
    "How are you?":["I'm good, thanks for asking!"]
}

# Add a dictionary of patterns and responses
pattern_responses = {
    "Do you remember (.*)":["Of course I remember {}","Yes, I do remember {}","Now that you mention it, I do remember {}"],
    "I feel (.*)":["Why do you feel {}", "You feel {}, why?","How long have you been feeling {}"]
}

def check_pattern(message):
    for pattern in pattern_responses:
        match = re.search(pattern, message)
        if match:
            # return the substring without the pattern
            answer = random.choice(pattern_responses[pattern])
            return answer.format(match.group(1))

def respond(message):
    if message in responses:
        return random.choice(  responses[message]  )    
    elif check_pattern(message):
        return "{}".format(check_pattern(message))
    else:
        return "I didn't get that: {}".format(message)

def send_message(message):
    print("USER: {}".format(message))
    wait_time = random.randint(1,4)
    time.sleep(wait_time)    
    print("Echobot: {}".format(respond(message)))

while True:
    send_message(input())