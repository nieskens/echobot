# COMPUTING & COGNITION
# ECHOBOT v0.1

# Define a function that responds to a user's message: respond
def respond(message):
    # Concatenate the user's message to the end of a standard bot respone
    bot_message = "I can hear you! You said: {}".format(message)
    # Return the result
    return bot_message

# Call the function respond an pass a message
print(respond("Hi!"))
