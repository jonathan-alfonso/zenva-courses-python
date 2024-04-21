from turtle import *

def move_and_turn (angle):
  forward(50)
  right(angle)

for x in range (12):
  move_and_turn(30)

done()