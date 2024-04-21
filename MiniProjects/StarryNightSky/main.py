from turtle import *
from random import *

speed(0)
bgcolor("black")
hideturtle()

# Get width and height of the window
width = window_width()
height = window_height()

# Draw a star at a given position
def draw_star (xpos, ypos):
  # Generate random size for the star
  size = randrange(2, 30)

  # Go to the given position
  penup()
  goto(xpos, ypos)
  pendown()

  # Draw the star
  dot(size, "white")

for x in range(100):
  # Create a random X & Y position
  xpos = randrange(round(-width / 2), round(width / 2))
  ypos = randrange(round(-height / 2), round(height / 2))

  # Draw the star at the given position
  draw_star(xpos, ypos)



done()