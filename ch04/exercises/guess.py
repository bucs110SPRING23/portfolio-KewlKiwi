import random

value = random.randrange(1, 1000)
numguesses = 0

while 1 == 1:
    guess = int(input("Please Enter a Guess: "))
    numguesses += 1
    if value == guess:
        break
    elif value > guess:
        print("Too Low")
    else:
        print("Too High")

print("It took you " + str(numguesses) + " tries to guess the correct value of " + str(value) + ".")
