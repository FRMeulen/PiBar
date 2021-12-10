import json
from types import SimpleNamespace

class User:
    def __init__(self, name, code, balance):
        self.name = name
        self.code = code
        self.balance = balance

    def to_json(self):
        return json.dumps(self, default=lambda d: d.__dict__, sort_keys=True, indent=4)

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
        self.users = json.loads(str_users, object_hook = lambda d: User(**d))

    def validate(self):
        for user in self.users:
            if user.code == self.user_code:
                print(f'Hallo, {user.name}!')
                print(f'Je hebt nog {user.balance} beschikbaar!')
                return user

        return 0

class UserSaver:
    filePath = './res/Users.json'

    def __init__(self, updated_user):
        self.updated_user = updated_user
        f = open(self.filePath)
        str_users = f.read()
        self.users = json.loads(str_users, object_hook = lambda d: User(**d))

    def update_in_memory(self):
        for index, user in enumerate(self.users):
            if user.code == self.updated_user.code:
                self.users[index] = self.updated_user

    def save(self):
        with open(self.filePath, 'w') as outputFile:
            outputFile.write(json.dumps(self.users, default=lambda d: d.__dict__, indent=4))
