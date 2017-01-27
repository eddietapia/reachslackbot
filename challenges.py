"""
File name: challenges.py
Author: Code Team @SHPEUCSD
Date: 1/22/17
Purpose: Handles the different challenges that we will give the
teams at SHPE's REACh 2017 Engineering Competition
"""

CHALLENGE_IMAGE_URL = "https://dl.dropboxusercontent.com/u/14766850/download%20%281%29.png"
CHALLENGE1_URL = "https://drive.google.com/file/d/0B9U4IYtGjEsVaktPSm1FRU82Wkk/view"
CHALLENGE2_URL = "https://drive.google.com/file/d/0B9U4IYtGjEsVdEtld2NDaGpCV0U/view"
CHALLENGE3_URL = "https://drive.google.com/file/d/0B9U4IYtGjEsVeXZOSnBiV2tpbjA/view"
CHALLENGE4_URL = "https://drive.google.com/file/d/0B9U4IYtGjEsVc3h5V2NwU19xOW8/view"
PUZZLE_1_URL = "https://drive.google.com/open?id=0B9U4IYtGjEsVcU1pZEJsTGlMMzQ"
PUZZLE_2_URL = "https://drive.google.com/open?id=0B9U4IYtGjEsVOWtVUTZCNmdGQ3c"
PUZZLE_3_URL = "https://drive.google.com/open?id=0B9U4IYtGjEsVY1lxTWlzeENVb00"
PUZZLE_4_URL = "https://drive.google.com/open?id=0B9U4IYtGjEsVV2ZLcWdJd2UzSE0"
CHALLENGE1_TEXT = "In order to unlock challenge 1, you need to solve a puzzle first...\nPlease tell the reachbot the answer to unlock the first challenge.\nEx: '@reachbot challenge 1 <answer>'"

def challenge0(params):
  if params is None:
    response = "In order to unlock challenge 0, you need to solve a puzzle first:" + \
           "\n\nPuzzle 0: " + "\nWhat is brown and sticky?\n" + \
            "\nPlease tell the reachbot the answer to unlock challenge 0" + \
            "\nEx: '@reachbot challenge 0 answer'"
    return response
  print type(params)
  user_answer = str(''.join(params))
  if "stick" in user_answer.lower():
      return  [

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
  return  [

                {

                        "fallback": "Puzzle 0 Not Completed",

                        "color": "#3652a6",

                        "pretext": "Wrong Answer!",

                        "title": "Better luck next time!",

                        "title_link": "http://giphy.com/gifs/colbertlateshow-no-stephen-colbert-l2JhLaxhWba6OivE4",

                        "text": "Congrats on finishing the example challenge",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]


def challenge1(params):
  if params is None:
    return  [

                {

                        "fallback": "Puzzle 1",

                        "color": "#3652a6",

                        "pretext": "REACh 2017",

                        "title": "Link to Puzzle 1",

                        "title_link": PUZZLE_1_URL,

                        "text": CHALLENGE1_TEXT,

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]

  user_answer = params[0]  
  # Check if user inputted correct answer 
  if "941" == user_answer:
        return  [

                {

                        "fallback": "Puzzle 1 Completed",

                        "color": "#3652a6",

                        "pretext": "REACh 2017",

                        "title": "Link to Challenge 1",

                        "title_link": CHALLENGE1_URL,

                        "text": "This challenge is due at 8:45pm",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]
  return  [

                {

                        "fallback": "Oops!",

                        "color": "#3652a6",

                        "pretext": "Wrong Answer!",

                        "title": "Wrong Answer! Your answer: " + user_answer,

                        "title_link": "http://giphy.com/gifs/colbertlateshow-no-stephen-colbert-l2JhLaxhWba6OivE4",

                        "text":  "This is supposed to be the easiest puzzle you know...",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]  
def challenge2(params):
  if params is None:
    return  [

                {

                        "fallback": "Puzzle 2",

                        "color": "#3652a6",

                        "pretext": "REACh 2017",

                        "title": "Link to Puzzle 2",

                        "title_link": PUZZLE_2_URL,

                        "text": "In order to unlock challenge 2, you need to solve a puzzle first..." + \
                        "\nPlease tell the reachbot the answer to unlock the second challenge." + \
                        "\nEx: '@reachbot challenge 2 <answer>'",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]
  if type(params) is str:
        user_answer = str(''.join(params))
  # Check if user inputted correct answer 
  if type(params) is str and "T" == user_answer:
        return  [

                {

                        "fallback": "Task assigned for challenge 2 is complete.",

                        "color": "#3652a6",

                        "pretext": "REACh 2017",

                        "title": "Link to Challenge 2",

                        "title_link": CHALLENGE2_URL,

                        "text": "This challenge is due at 6am",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]
  return  
  {
            "attachments": [
              {
                      "fallback": "Oops!",
                      "color": "#ff0000",
                      "pretext": "Wrong Answer!",
                      "title": "Wrong Answer! I could do this for days",
                      "title_link": "http://giphy.com/gifs/colbertlateshow-no-stephen-colbert-l2JhLaxhWba6OivE4",
                      "text": "Let me know if you need my help... I'm kind of a genius'",
                      "footer": "REACh",
                      "footer_icon": CHALLENGE_IMAGE_URL
              }
            ]
          }

def challenge3(params):
  if params is None:
    return [

                {

                        "fallback": "Task assigned for challenge 3 is complete.",

                        "color": "#3652a6",

                        "pretext": "REACh 2017",

                        "title": "Link to Puzzle 3",

                        "title_link": PUZZLE3_URL,

                        "text": "In order to unlock challenge 3, you need to solve a puzzle first..." + \
                        "\nPlease tell the reachbot the answer to unlock the third challenge." + \
                        "\nEx: '@reachbot challenge 3 <answer>'",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ] 
  if type(params) is str:
        user_answer = str(''.join(params))
  # Check if user inputted correct answer 
  if type(params) is int and 5 == user_answer:
    return [

                {

                        "fallback": "Task assigned for challenge 3 is complete.",

                        "color": "#3652a6",

                        "pretext": "REACh 2017",

                        "title": "Link to Challenge 3",

                        "title_link": CHALLENGE3_URL,

                        "text": "This challenge is due at 10am",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]
    return [

                {

                        "fallback": "Oops!",

                        "color": "#ff0000",

                        "pretext": "Wrong Answer!",

                        "title": "Wrong Answer buddy! Nice try.",

                        "title_link": "http://giphy.com/gifs/colbertlateshow-no-stephen-colbert-l2JhLaxhWba6OivE4",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]
           
def challenge4(params):
  if params is None:
     return [

                {

                        "fallback": "Puzzle 4",

                        "color": "#3652a6",

                        "pretext": "REACh 2017",

                        "title": "Link to Puzzle 4",

                        "title_link": PUZZLE4_URL,

                        "text": "In order to unlock challenge 4, you need to solve a puzzle first..." + \
                        "\nPlease tell the reachbot the answer to unlock the third challenge." + \
                        "\nEx: '@reachbot challenge 4 <answer>'",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]    
  if type(params) is str:
        user_answer = str(''.join(params))
  # Check if user inputted correct answer 
  if type(params) is int and 2016 == user_answer:
    return  [

                {

                        "fallback": "Puzzle 4 is completed",

                        "color": "#3652a6",

                        "pretext": "REACh 2017",

                        "title": "Link to Challenge 4",

                        "title_link": CHALLENGE4_URL,

                        "text": "This challenge is due at 6pm",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]        
  return  [

                {

                        "fallback": "Oops!",

                        "color": "#ff0000",

                        "pretext": "Wrong Answer!",

                        "title": "Wrong Answer buddy! Nice try.",

                        "title_link": "http://giphy.com/gifs/colbertlateshow-no-stephen-colbert-l2JhLaxhWba6OivE4",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]  