from classes.User import UserSaver

class TransactionHandler:
    def __init__(self, user, drink):
        self.user = user
        self.drink = drink

    def check(self):
        if self.user.balance < self.drink.price:
            return False

        return True

    def handle(self):
        self.user.balance -= self.drink.price
        print('Je hebt', self.drink.name, 'gekocht voor', str(self.drink.price) + '.')
        print('Er staat nog', self.user.balance, 'op je kaart.')
        # ToDo: Log the transaction here

        saver = UserSaver(self.user)
        saver.update_in_memory()
        saver.save()
