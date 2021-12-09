import json
from types import SimpleNamespace

class DrinksValidator:
    filePath = './res/Drinks.json'

    def __init__(self, drink_code):
        self.drink_code = drink_code
        f = open(self.filePath)
        str_drinks = f.read()
        self.drinks = json.loads(str_drinks, object_hook = lambda d: SimpleNamespace(**d))

    def validate(self):
        for drink in self.drinks:
            if drink.code == self.drink_code:
                print(drink.name + ',', 'goede keuze!')
                return drink

        print('Error: Drink code invalid!')
        quit()
