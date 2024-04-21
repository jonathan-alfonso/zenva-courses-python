health = 100
damage = 20
life_potion = 50

print("Starting health: " + str(health))

health -= damage
print("Health after sub: " + str(health))

health += life_potion
print("Health after add: " + str(health))

health = health * 1.5
print("Health after multiply: " + str(health))

health = health / 2
print("Health after divide: " + str(health))