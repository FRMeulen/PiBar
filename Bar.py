from classes.UserValidator import UserValidator

print('Scan je kaart: ', end='')
user_code = input()
user_validator = UserValidator(user_code)
user = user_validator.validate()

if user == 'Error':
    print(user)
    quit()

print('Hallo', user.name + '!')
