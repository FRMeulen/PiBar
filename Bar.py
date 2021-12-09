from classes.UserValidator import UserValidator
from classes.DrinksValidator import DrinksValidator

print('Scan je kaart: ', end='')
user_code = input()
user_validator = UserValidator(user_code)
user = user_validator.validate()

if user == 'Error':
    print(user)
    quit()

print('Hallo', user.name + '!')
print('Scan je drankje: ', end='')
drink_code = input()
drinks_validator = DrinksValidator(drink_code)
drink = drinks_validator.validate()

if drink == 'Error':
    print('Error: Drink not found!')
    quit()

print('Ah lekker!', drink.name + '!')
