# COMPUTING & COGNITION
# ECHOBOT v0.2 Including SQLite database

import sqlite3 as lite
import sys

import time
import random

bot_is_waiting = True

# SQLite connection
conn = None
try:
    conn = lite.connect('echobot_db.db')
    print("Opened database")
    '''
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print("SQLite version: {}".format(data))
    '''
except: 
    print("Error")
    sys.exit(1)

finally:
    if conn:
        conn.close()



# A dictionary of bot responses
responses = {
            "Hello":"Hi!",
            "What's your name?":"My name is EchoBot.",
            "How are you?":"I'm good, thanks!",
            "How old are you?":"Wouldn't you wanna know!?"
            }


# Define a function that responds to a user's message: respond
def respond(message):
    # Concatenate the user's message to the end of a standard bot respone
    if message in responses:
        bot_message = responses[message]
    else:
        bot_message = "I can hear you! You said: {}".format(message)
    return bot_message

# Define a function that sends the message and prints both user and bot's answers
def send_message(message):
    print("YOU: {}".format(message))
    time.sleep(random.randint(1,3))
    print("ECHOBOT: {}".format(respond(message)))

# Call the function send_message to start the dialogue
#while bot_is_waiting:
send_message("DB test")
