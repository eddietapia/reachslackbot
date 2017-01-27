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
      return [
                {
                  "fallback": "Task assigned after Challenge 0 is complete.",
                  "color": "#3652a6",
                  "pretext": "REACh 2017 Challenge 0 Completed",
                  "title": "Link to Challenge 0",
                  "title_link": "http://gph.is/2ewaKoM",
                  "text": "Congrats on finishing the example challenge!!!",
                  "footer": "REACh",
                  "footer_icon": CHALLENGE_IMAGE_URL
                }
            ]
  return [
          {
            "fallback": "Task assigned after Challenge 1 is complete.",
            "color": "#ff0000",
            "pretext": "Wrong Answer!",
            "title": "Better luck next time!",
            "title_link": "http://giphy.com/gifs/colbertlateshow-no-stephen-colbert-l2JhLaxhWba6OivE4",
            "footer": "REACh",
            "footer_icon": CHALLENGE_IMAGE_URL
          }
        ]

def challenge1(params):
 if params is None:
    return [
            {
              "fallback": "Task assigned after Challenge 1 is complete.",
              "color": "#3652a6",
              "pretext": "REACh 2017 Challenge 1 Task Completed",
              "title": "Link to Puzzle 1",
              "title_link": PUZZLE_1_URL,
              "text": "In order to unlock challenge 1, you need to solve a puzzle first..." + \
                "\nPlease tell the reachbot the answer to unlock the first challenge." + \
                "\nEx: '@reachbot challenge 1 <answer>'",
              "footer": "REACh",
              "footer_icon": CHALLENGE_IMAGE_URL
            }
            ] 
    #response = "In order to unlock challenge 1, you need to solve a puzzle first:" + \
           #"\nPuzzle 1: " + "\nWhat is brown and sticky?" + \
            #"\nPlease tell the reachbot the answer to unlock the first challenge." + \
            #"\nEx: '@reachbot challenge 1 answer'"
    return response
  print type(params)
  user_answer = str(''.join(params))
  # Check if user inputted correct answer 
  if "941" == user_answer:
        return [
                {
                  "fallback": "Task assigned after Challenge 1 is complete.",
                  "color": "#3652a6",
                  "pretext": "REACh 2017 Challenge 1 Task Completed",
                  "title": "Link to Challenge 1",
                  "title_link": CHALLENGE1_URL,
                  "text": "This challenge is due at 8:45pm",
                  "footer": "REACh",
                  "footer_icon": CHALLENGE_IMAGE_URL
                }
               ] 
  return [
          {
                  "fallback": "Oops!",
                  "color": "#ff0000",
                  "pretext": "Wrong Answer!",
                  "title": "Wrong Answer!",
                  "title_link": "http://giphy.com/gifs/colbertlateshow-no-stephen-colbert-l2JhLaxhWba6OivE4",
                  "text": "This is supposed to be the easiest puzzle you know..."
                  "footer": "REACh",
                  "footer_icon": CHALLENGE_IMAGE_URL
          }
        ]
def challenge2(params):
 if params is None:
    return [
            {
              "fallback": "Task assigned after Challenge 2 is complete.",
              "color": "#3652a6",
              "pretext": "REACh 2017 Challenge 2 Task Completed",
              "title": "Link to Puzzle 2",
              "title_link": PUZZLE_2_URL,
              "text": "In order to unlock challenge 2, you need to solve a puzzle first..." + \
                "\nPlease tell the reachbot the answer to unlock the second challenge." + \
                "\nEx: '@reachbot challenge 2 <answer>'",
              "footer": "REACh",
              "footer_icon": CHALLENGE_IMAGE_URL
            }
            ] 
  print type(params)
  user_answer = str(''.join(params))
  # Check if user inputted correct answer 
  if "T" == user_answer:
        return [
                {
                  "fallback": "Task assigned for Challenge 2 is complete.",
                  "color": "#3652a6",
                  "pretext": "REACh 2017 Challenge 2 Task Completed",
                  "title": "Link to Challenge 2",
                  "title_link": CHALLENGE2_URL,
                  "text": "This challenge is due at 6am",
                  "footer": "REACh",
                  "footer_icon": CHALLENGE_IMAGE_URL
                }
               ] 
  return [
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

def challenge3(params):
  if params is None:
    return [
            {
              "fallback": "Task assigned after Challenge 3 is complete.",
              "color": "#3652a6",
              "pretext": "REACh 2017 Challenge 3 Task Completed",
              "title": "Link to Puzzle 3",
              "title_link": PUZZLE_3_URL,
              "text": "In order to unlock challenge 3, you need to solve a puzzle first..." + \
                "\nPlease tell the reachbot the answer to unlock the third challenge." + \
                "\nEx: '@reachbot challenge 3 <answer>'",
              "footer": "REACh",
              "footer_icon": CHALLENGE_IMAGE_URL
            }
            ] 
  print type(params)
  user_answer = str(''.join(params))
  # Check if user inputted correct answer 
  if "5" == user_answer:
        return [
                {
                  "fallback": "Task assigned for Challenge 3 is complete.",
                  "color": "#3652a6",
                  "pretext": "REACh 2017 Challenge 3 Task Completed",
                  "title": "Link to Challenge 3",
                  "title_link": CHALLENGE3_URL,
                  "text": "This challenge is due at 10:00am",
                  "footer": "REACh",
                  "footer_icon": CHALLENGE_IMAGE_URL
                }
               ] 
  return [
          {
                  "fallback": "Oops!",
                  "color": "#ff0000",
                  "pretext": "Wrong Answer!",
                  "title": "Wrong Answer! Nice try. ",
                  "title_link": "http://giphy.com/gifs/colbertlateshow-no-stephen-colbert-l2JhLaxhWba6OivE4",
                  "footer": "REACh",
                  "footer_icon": CHALLENGE_IMAGE_URL
          }
        ]
def challenge4(params):
  if params is None:
    return [
            {
              "fallback": "Task assigned after Challenge 4 is complete.",
              "color": "#3652a6",
              "pretext": "REACh 2017 Challenge 4 Task Completed",
              "title": "Link to Puzzle 4",
              "title_link": PUZZLE_4_URL,
              "text": "In order to unlock challenge 4, you need to solve a puzzle first..." + \
                "\nPlease tell the reachbot the answer to unlock the first challenge." + \
                "\nEx: '@reachbot challenge 4 <answer>'",
              "footer": "REACh",
              "footer_icon": CHALLENGE_IMAGE_URL
            }
            ] 
  print type(params)
  user_answer = str(''.join(params))
  # Check if user inputted correct answer 
  if "2016" == user_answer:
        return [
                {
                  "fallback": "Task assigned for Challenge 4 is complete.",
                  "color": "#3652a6",
                  "pretext": "REACh 2017 Challenge 4 Task Completed",
                  "title": "Link to Challenge 4",
                  "title_link": CHALLENGE4_URL,
                  "text": "This challenge is due at 6pm",
                  "footer": "REACh",
                  "footer_icon": CHALLENGE_IMAGE_URL
                }
               ] 
  return [
          {
                  "fallback": "Oops!",
                  "color": "#ff0000",
                  "pretext": "Wrong Answer!",
                  "title": "Wrong!!!",
                  "title_link": "http://giphy.com/gifs/colbertlateshow-no-stephen-colbert-l2JhLaxhWba6OivE4",
                  "text": "Close! But not close enough... Please try again",
                  "footer": "REACh",
                  "footer_icon": CHALLENGE_IMAGE_URL
          }
        ]