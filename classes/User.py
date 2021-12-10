import json
from types import SimpleNamespace

class UserInput:
    def get_user(self):
        print('Hallo, scan je kaart: ', end='')
        self.user_code = input()
        return self.user_code

class UserValidator:
    filePath = './res/Users.json'

    def __init__(self, user_code):
        self.user_code = user_code
        f = open(self.filePath)
        str_users = f.read()
        self.users = json.loads(str_users, object_hook = lambda d: SimpleNamespace(**d))

    def validate(self):
        for user in self.users:
            if user.code == self.user_code:
                print('Hallo', user.name + '!')
                print('Je hebt nog ', user.balance, 'beschikbaar!')
                return user

        return 0
