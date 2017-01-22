CHALLENGE_IMAGE_URL = "https://dl.dropboxusercontent.com/u/14766850/download%20%281%29.png"
def challenge0(params):
  if params is None:
    response = "In order to unlock challenge 1, you need to solve a puzzle first:" + \
           "\nPuzzle 0: " + "\nWhat is brown and sticky?" + \
            "\nPlease tell the reachbot the answer to unlock the first challenge." + \
            "\nEx: '@reachbot challenge 0 answer'" 
    return response
  print type(params)
  user_answer = str(''.join(params))
  
  if "stick" in user_answer.lower():
        return [

                {

                        "fallback": "Task assigned after Challenge 1 is complete.",

                        "color": "#3652a6",

                        "pretext": "REACh 2017 Challenge 1 Completed",

                        "title": "Link to Challenge",

                        "title_link": "https://drive.google.com/open?id=0B9U4IYtGjEsVaktPSm1FRU82Wkk",

                        "text": "This challenge is due at 8:45pm",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ] 
def challenge1(params):
  if params is None:
    return "challenge 1 goes here"
def challenge2(params):
  if params is None:
    return "challenge 2 goes here"
def challenge3(params):
  if params is None:
    return "challenge 3 goes here"
def challenge4(params):
  if params is None:
    return "challenge 4 goes here"


