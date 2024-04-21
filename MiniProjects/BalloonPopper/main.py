from turtle import *

# Variables
balloon_size = 40
balloon_pop = 300
pops = 0

# Functions
def draw_balloon ():
  if pops == 0:
    balloon_color = "green"
  elif (pops > 0) and (pops < 5):
    balloon_color = "orange"
  else:
    balloon_color = "red"
  color(balloon_color)
  dot(balloon_size)

def inflate_balloon ():
  global balloon_size
  balloon_size = balloon_size + 10
  draw_balloon()

  if balloon_size >= balloon_pop:
    clear()
    balloon_size = 40
    write("POP!")
    global pops
    pops += 1
    print("Pops: " + str(pops))

def deflate_balloon ():
  global balloon_size
  balloon_size = balloon_size - 10
  clear()
  draw_balloon()

  if balloon_size <= 0:
    clear()
    balloon_size = 40
    write("FLOP!")

# Calls
draw_balloon()

onkey(inflate_balloon, "Up")
onkey(deflate_balloon, "Down")

listen()

done()