import time
from classes.User import UserInput, UserValidator
from classes.Drink import DrinkInput, DrinkValidator
from classes.Transaction import TransactionHandler

def clear_console():
    print(chr(27) + '[2J')

def reset_app(message):
    print(message)
    print('Restart over 5 seconden...')
    time.sleep(5)
    clear_console()

def run_bar():
    user_input = UserInput()
    user_code = user_input.get_user()
    user_validator = UserValidator(user_code)
    user = user_validator.validate()
    if user == 0:
        reset_app('Error: Gebruiker niet gevonden!')

    drink_input = DrinkInput()
    drink_code = drink_input.get_drink()
    drink_validator = DrinkValidator(drink_code)
    drink = drink_validator.validate()
    if drink == 0:
        reset_app('Error: Drankje niet gevonden!')

    transaction_handler = TransactionHandler(user, drink)
    if transaction_handler.check():
        transaction_handler.handle()
        reset_app('Geniet van je drankje!')
    else:
        reset_app('Error: Niet genoeg saldo!')

clear_console()
while True:
    run_bar()
