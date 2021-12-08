import json
from types import SimpleNamespace

class UserValidator:
    filePath = './res/Users.json'

    def __init__(self, user_code):
        self.user_code = user_code
        f = open(self.filePath)
        str_users = f.read()
        self.json = json.loads(str_users, object_hook = lambda d: SimpleNamespace(**d))

    def test(self):
        print('Type: ', type(self.users))
        print(self.json.users[0])

    def validate(self):
        for user in self.json.users:
            if user.code == self.user_code:
                return user

        return 'Error'
