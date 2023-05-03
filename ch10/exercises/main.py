import requests
import random

class TriviaProxyAPI:

    def __init__(self):
        self.url = "https://opentdb.com/api.php?"
        self.varstr = "amount=1&category=18"

    def get(self):
        url = self.url + self.varstr
        response = requests.get(url)
        data = response.json
        print(data)
        return data

def main():
    tp = TriviaProxyAPI()
    results = tp.get()

    response = requests.get("https://opentdb.com/api.php?amount=1&category=17")
    data = response.json()
    results = data['results']

    for r in results:
        print(r['question'])
        possibles = [r["correct_answer"]] + r["incorrect_answers"]
        random.shuffle(possibles)
        print("Make your selection: ")
        for i, p in enumerate(possibles):
            print(f"{i}) {p} ")

        selection = input(":")

        if len(possibles) == 4 and (selection != "0" and selection != "1" and selection != "2" and selection != "3"):
            print("Error")
        elif len(possibles) == 2 and (selection != "0" and selection != "1"):
            print("Error")
        elif possibles[int(selection)] == r["correct_answer"]:
            print("correct answer")
        else:
            print("incorrect")

main()