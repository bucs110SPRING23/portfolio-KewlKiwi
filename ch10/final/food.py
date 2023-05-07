import requests

class Food:

    def __init__(self):
        self.url = "https://www.themealdb.com/api/json/v1/1/random.php"

    def get(self):
        response = requests.get(self.url)
        data = response.json()
        if data.get('meals'):
            return data['meals']
        else:
            return None