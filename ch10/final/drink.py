import requests

class Drink:

    def __init__(self):
        self.url = "http://www.thecocktaildb.com/api/json/v1/1/random.php"

    def get(self):
        response2 = requests.get(self.url)
        data = response2.json()
        if data.get('drinks'):
           return data['drinks']
        else:
            return None