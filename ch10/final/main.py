import food
import drink

def main():
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
          meal.ingredients(data1)
     elif response == "b":
          beverage.ingredients(data2)
     elif response == "c":
          meal.recipe(data1)
     elif response == "d":
          beverage.recipe(data2)
     elif response == "q":
        view = False

main()