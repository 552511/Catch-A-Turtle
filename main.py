# INSTRUCTIONS:
#   TODO 1:
#   Run this code and click on the circle a few times. Document what happens, or
#   doesn't happen. Stop the code and observe the error message. Document what 
#   you think this means.
#
#   TODO 2:
#   Run this code again and click on the square a few times. Document what 
#   happens in the python console. Stop the code. 

import turtle as trtl
import random as rand

score = 0 

# circular turtle will not use a global variable
spot = trtl.Turtle()
spot.goto(-100, 0)
spot.shape("circle")
spot.shapesize(3)

# square shaped turtle will use a global variable
box = trtl.Turtle()
box.goto(100,0)
box.shape("square")
box.shapesize(3)

def update_score():
    global score 
    score = 1 + score
    print(score)

def spot_clicked(x,y):
  print("clicked")
  update_score()
  change_position()

def change_position():
  spot.penup()
  spot.showturtle
  new_xpos=rand.randint(-200, 200)
  new_ypos=rand.randint(-150, 150)
  spot.goto(new_xpos,new_ypos)
  spot.pendown()
  spot.hideturtle
  score = 0
score(0, 0)
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()