from classes.UserInput import UserInput
from classes.UserValidator import UserValidator
from classes.DrinksInput import DrinksInput
from classes.DrinksValidator import DrinksValidator
from classes.TransactionChecker import TransactionChecker

def reset_app():
    os.execv(sys.argv[0], sys.argv)

user_input = UserInput()
user_code = user_input.get_user()
user_validator = UserValidator(user_code)
user = user_validator.validate()

drinks_input = DrinksInput()
drink_code = drinks_input.get_drink()
drinks_validator = DrinksValidator(drink_code)
drink = drinks_validator.validate()

transaction_checker = TransactionChecker(user, drink)
print(transaction_checker.check())
