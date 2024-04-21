import random

temp = random.random() * 100
target = random.random() * 100

print("Temp: " + str(temp))
print("Target: " + str(target))

if temp > target:
  print("Too hot!")
elif temp < target:
  print("Too cold!")