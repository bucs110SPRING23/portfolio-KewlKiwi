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
        data = response.json()
        if data.get('meals'):
            return data['meals']
        else:
            return None