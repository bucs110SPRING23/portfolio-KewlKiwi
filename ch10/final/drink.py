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