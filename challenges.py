"""
File name: challenges.py
Author: Code Team @SHPEUCSD
Date: 1/22/17
Purpose: Handles the different challenges that we will give the
teams at SHPE's REACh 2017 Engineering Competition
"""

CHALLENGE_IMAGE_URL = "https://dl.dropboxusercontent.com/u/14766850/download%20%281%29.png"
CHALLENGE1_URL = "https://drive.google.com/file/d/0B01WlOybAVzdVmdaVjBNMnRMeDA/view"
CHALLENGE2_URL = "https://drive.google.com/file/d/0B01WlOybAVzdaXV2X01wVmhpUU0/view"
CHALLENGE3_URL = "https://drive.google.com/file/d/0B01WlOybAVzdRS1qNnVLYjRKT1k/view"
CHALLENGE4_URL = "https://drive.google.com/file/d/0B01WlOybAVzdd2cyQ1ljU0VhTWs/view"
PUZZLE_1_URL = "https://drive.google.com/file/d/0B9U4IYtGjEsVQzRXTzMxelZ6TlU/view"
PUZZLE_2_URL = "https://drive.google.com/open?id=0B9U4IYtGjEsVOWtVUTZCNmdGQ3c"
PUZZLE_3_URL = "https://drive.google.com/open?id=0B9U4IYtGjEsVY1lxTWlzeENVb00"
PUZZLE_4_URL = "https://drive.google.com/open?id=0B9U4IYtGjEsVV2ZLcWdJd2UzSE0"
PUZZLE_SECRET_1 = "https://docs.google.com/document/d/1brcNj2Ml0IwBxQUUSQUJ7JJAq6w1Znd2J5s0P19YVvY/edit?usp=sharing"
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
  # Check if correct answer
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

  user_answer = str(params[0])  
  # Check if user inputted correct answer 
  if len(params) == 1 and "64" == user_answer:
        return  [

                {

                        "fallback": "Puzzle 1 Completed",

                        "color": "#3652a6",

                        "pretext": "REACh 2017",

                        "title": "Link to Challenge 1",

                        "title_link": CHALLENGE1_URL,

                        "text": "Congrats you got it!\n This challenge is due at 8:45pm",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]
  return  [

                {

                        "fallback": "Oops!",

                        "color": "#ff0000",

                        "pretext": "Wrong Answer!",

                        "title": "Wrong Answer!",

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
  user_answer = params[0]
  print len(params)
  print params[0]
  # Check if user inputted correct answer 
  if len(params) == 1 and "T" == user_answer:
        return  [

                {

                        "fallback": "Task assigned for challenge 2 is complete.",

                        "color": "#3652a6",

                        "pretext": "REACh 2017",

                        "title": "Link to Challenge 2",

                        "title_link": CHALLENGE2_URL,

                        "text": "Congrats on finishing puzzle 2!\nThis challenge is due at 6am",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]
  return  [

                {

                        "fallback": "Oops!",

                        "color": "#ff0000",

                        "pretext": "Wrong Answer!",

                        "title": "Wrong Answer!",

                        "title_link": "http://giphy.com/gifs/colbertlateshow-no-stephen-colbert-l2JhLaxhWba6OivE4",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]  

def challenge3(params):
  if params is None:
    return [

                {

                        "fallback": "Task assigned for challenge 3 is complete.",

                        "color": "#3652a6",

                        "pretext": "REACh 2017",

                        "title": "Link to Puzzle 3",

                        "title_link": PUZZLE_3_URL,

                        "text": "In order to unlock challenge 3, you need to solve a puzzle first..." + \
                        "\nPlease tell the reachbot the answer to unlock the third challenge." + \
                        "\nEx: '@reachbot challenge 3 <answer>'",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ] 
  user_answer = params[0]
  # Check if user inputted correct answer 
  if len(params) == 1 and "5" == user_answer:
    return [

                {

                        "fallback": "Task assigned for challenge 3 is complete.",

                        "color": "#3652a6",

                        "pretext": "REACh 2017",

                        "title": "Link to Challenge 3",

                        "title_link": CHALLENGE3_URL,

                        "text": "Congrats on finishing puzzle 3!\nThis challenge is due at 10am",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]
  return  [

                {

                        "fallback": "Oops!",

                        "color": "#ff0000",

                        "pretext": "Wrong Answer!",

                        "title": "Wrong Answer!",

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

                        "title_link": PUZZLE_4_URL,

                        "text": "In order to unlock challenge 4, you need to solve a puzzle first..." + \
                        "\nPlease tell the reachbot the answer to unlock the third challenge." + \
                        "\nEx: '@reachbot challenge 4 <answer>'",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]    
  user_answer = str(params[0])
  # Check if user inputted correct answer 
  if len(params) == 1 and "2016" == user_answer:
    return  [

                {

                        "fallback": "Puzzle 4 is completed",

                        "color": "#3652a6",

                        "pretext": "REACh 2017",

                        "title": "Link to Challenge 4",

                        "title_link": CHALLENGE4_URL,

                        "text": "Congrats on finishing puzzle 4!\nThis challenge is due at 6pm",

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
def challenge5(params):
  if params is None:
    return [

                {

                        "fallback": "Secret challenge",

                        "color": "#3652a6",

                        "pretext": "REACh 2017",

                        "title": "Secret Coding Challenge",

                        "title_link": PUZZLE_SECRET_1,

                        "text": "Let Eddie know when you are done \n- Happy hacking",

                        "footer": "REACh",

                        "footer_icon": CHALLENGE_IMAGE_URL

                }

           ]