import random
random_number = random.random()
print("Random number is: ", random_number)
random_number = random.random()
if random.random() < 0.25:
    print("try to go right")
elif random.random() > 0.25 and random_number < 0.5:
    print("try to go left")
elif random.random() > 0.5 and random_number < 0.75:
    print("try to go left")
else:
    print("try to go bottom")