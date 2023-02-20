import random

number = random.randrange(1, 11)

for _ in range(3):
   guess = int(input("Please enter a guess:"))
   if guess == number:
    print("Correct")
    break
   elif guess <= number:
    print("Too Low")
   else:
    print("Too High")


