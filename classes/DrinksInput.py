class DrinksInput:
    def get_drink(self):
        print('Scan je drankje: ', end='')
        self.drink_code = input()
        return self.drink_code
