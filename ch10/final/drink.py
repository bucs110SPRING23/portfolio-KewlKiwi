import requests

class Drink:

    def __init__(self):
        """
        Initializes the drink object with the url for a random drink
        args: None
        return: None
        """
        self.url = "http://www.thecocktaildb.com/api/json/v1/1/random.php"

    def get(self):
        """
        Gets data from the url and returns it
        args: None
        return: (list) list with keys and values from the url including the name, recipe, and ingredients
        """
        response2 = requests.get(self.url)
        data = response2.json()
        if data.get('drinks'):
           return data['drinks']
        else:
            return None
        
    def ingredients(self, data2):
        """
        Prints ingredients in the drink
        args: (dictionary) dictionary containing the keys and values for the different ingredients
        return: None
        """
        data = data2
        print("")
        print("Drink Ingredients:")
        for _ in range(15):
            key2 = "strIngredient" + str(_ + 1)
            ingredients = data[key2]
            if ingredients == None:
                break
            print(ingredients)
    
    def recipe(self, data2):
        """
        Prints the recipe for the drink
        args: (dictionary) dictionary containing the string for the drink recipe
        return: None
        """
        data = data2
        print("")
        print("Drink Recipe:")
        instructions = data['strInstructions']
        print(instructions)