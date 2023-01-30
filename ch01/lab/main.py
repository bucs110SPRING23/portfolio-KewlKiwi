import random

#Part A
weeks = 16
print(weeks, type(weeks))

classes = 5
print(classes, type(classes))

tuition = 6000
print(tuition, type(tuition))

cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 5
print(classes_per_week, type(classes_per_week))

cost_per_class = cost_per_week/classes_per_week
print(cost_per_class, type(cost_per_class))
print("Your total cost per class is $", cost_per_class)



#Part B

choice1 = "Cat"
choice2 = "Dog"
choice3 = 7
choice4 = 678
choice5 = 45.2

list1 = choice1, choice2, choice3, choice4, choice5

randomChoice = random.choice(list1)

print(randomChoice)
