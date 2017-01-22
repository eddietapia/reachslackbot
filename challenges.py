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

                        "fallback": "Task assigned after Challenge 0 is complete.",

                        "color": "#3652a6",

                        "pretext": "REACh 2017 Challenge 0 Completed",

                        "title": "Congrats Gif",

                        "title_link": "http://gph.is/2ewaKoM",

                        "text": "Congrats on finishing the example challenge",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]
  return [

          {

                  "fallback": "Task assigned after Challenge 1 is complete.",

                  "color": "#ff0000",

                  "pretext": "Wrong Answer!",

                  "title": "Wrong Gif",

                  "title_link": "http://giphy.com/gifs/colbertlateshow-no-stephen-colbert-l2JhLaxhWba6OivE4",

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


