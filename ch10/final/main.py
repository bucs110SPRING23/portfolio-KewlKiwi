import food
import drink
import requests

def main():
    """
    Runs the program, gets results from get functions in drink.py and food.py and prints them to the screen. Allows the user to select whether they want to view meal ingredients, drink ingredients, or the recipes for both.
    args: None
    return: None
    """
    meal = food.Food()
    results1 = meal.get()
    beverage = drink.Drink()
    results2 = beverage.get()
    view = True

    
    for data1 in results1:
       dish = data1['strMeal']

    for data2 in results2:
        bev = data2['strDrink']

    print("Your meal is " + dish + " and your drink is " + bev)

    while view:
     print("")
     print("What would you like to view?")
     print("-Meal Ingredients (a)")
     print("-Drink Ingredients (b)")
     print("-Meal Recipe (c)")
     print("-Drink Recipe (d)")
     print("Quit (q)")
     print("")
     response = input()

     if response == "a":
          print("")
          print("Meal Ingredients:")
          for _ in range(20):
             key = "strIngredient" + str(_ + 1)
             ingredients1 = data1[key]
             if ingredients1 == None or ingredients1 == "":
                break
             print(ingredients1)
     elif response == "b":
         print("")
         print("Drink Ingredients:")
         for _ in range(15):
             key2 = "strIngredient" + str(_ + 1)
             ingredients2 = data2[key2]
             if ingredients2 == None:
                 break
             print(ingredients2)
     elif response == "c":
        print("")
        print("Meal Recipe:")
        instructions1 = data1['strInstructions']
        print(instructions1)
     elif response == "d":
        print("")
        print("Drink Recipe:")
        instructions2 = data2['strInstructions']
        print(instructions2)
     elif response == "q":
        view = False



main()