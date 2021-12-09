class UserInput:
    def get_user(self):
        print('Hallo, scan je kaart: ', end='')
        self.user_code = input()
        return self.user_code
