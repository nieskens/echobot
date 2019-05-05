# COMPUTING & COGNITION
# ECHOBOT v0.1

# Define a function that responds to a user's message: respond
def respond(message):
    # Concatenate the user's message to the end of a standard bot respone
    bot_message = "I can hear you! You said: {}".format(message)
    return bot_message

# Define a function that sends the message and prints both user and bot's answers
def send_message(message):
    print("YOU: {}".format(message))
    print("ECHOBOT: {}".format(respond(message)))

# Call the function send_message to start the diaglogue
send_message("Hi, how are you?")
