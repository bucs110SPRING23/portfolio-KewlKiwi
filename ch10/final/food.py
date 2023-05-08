import requests

class Food:

    def __init__(self):
        """
        Initializes the drink object with the url for a random drink
        args: None
        return: None
        """
        self.url = "https://www.themealdb.com/api/json/v1/1/random.php"

    def get(self):
        """
        Gets data from the url and returns it
        args: None
        return: (list) list with keys and values from the url including the name, recipe, and ingredients
        """
        response = requests.get(self.url)
        self.data = response.json()
        if self.data.get('meals'):
            self.var = self.data['meals']
            return self.data['meals']
        else:
            return None

    def ingredients(self, data1):
        """
        Prints ingredients in the meal
        args: (dictionary) dictionary containing the keys and values for the different ingredients
        return: None
        """
        data = data1
        print("")
        print("Meal Ingredients:")
        for _ in range(20):
         key = "strIngredient" + str(_ + 1)
         ingredients = data[key]
         if ingredients == None or ingredients == "":
             break
         print(ingredients)

    def recipe(self, data1):
        """
        Prints the recipe for the meal
        args: (dictionary) dictionary containing the string for the meal recipe
        return: None
        """
        data = data1
        print("")
        print("Meal Recipe:")
        instructions1 = data['strInstructions']
        print(instructions1)