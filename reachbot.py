import os
import time
from challenges import challenge0,challenge1,challenge2,challenge3,challenge4
from slackclient import SlackClient


# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"
HELP_COMMAND = "help"
CHALLENGE0_COMMAND = "challenge 0"
CHALLENGE1_COMMAND = "challenge 1"
CHALLENGE2_COMMAND = "challenge 2"
CHALLENGE3_COMMAND = "challenge 3"
CHALLENGE4_COMMAND = "challenge 4"
# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def handle_command(command, channel):
    """
    Receives commands directed at the bot and determines if they
    are valid commands. If so, then acts on the commands. If not,
    returns back what it needs for clarification.
    """
    response = "Hi! Welcome to REACh 2017!\n" + \
               "Please type '@reachbot help' for more info.\n" + \
               "Happy Hacking\n" + \
               "- Your friends at REACh"
    array_response = [] 
    # Split user params into an array 
    params = command.split(' ')
    
    if command.startswith(HELP_COMMAND):
      response = "This bot will be used to tell you the upcoming " + \
                  "challenges that each team has to complete.\nType '" + \
                  "@reachbot challenge [number]' to find out more info." + \
                  "\nEx: '@reachbot challenge 1' \n - Your friends at REACh"
    elif command.startswith(CHALLENGE0_COMMAND):
      if (len(params) >= 3):
        array_response = challenge0(params[2:])
      else:
        response = challenge0(None)
    elif command.startswith(CHALLENGE1_COMMAND):
      if (len(params) >= 3):
        array_response = challenge1(params[2:])
      else:
        response = challenge1(None)
    elif command.startswith(CHALLENGE2_COMMAND):
      if (len(params) >= 3):
        array_response = challenge2(params[2:])
      else:
        response = challenge2(None)
 
    elif command.startswith(CHALLENGE3_COMMAND):
      if (len(params) >= 3):
        array_response = challenge3(params[2:])
      else:
        response = challenge3(None)
    elif command.startswith(CHALLENGE4_COMMAND):
      if (len(params) >= 3):
        array_response = challenge4(params[2:])
      else:
        response = challenge4(None)


    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"
    if len(array_response) is 0:
      slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
    else:
      slack_client.api_call("chat.postMessage", channel=channel,
                          attachments=array_response, as_user=True)
      


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("ReachBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
