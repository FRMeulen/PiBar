class TransactionChecker:
    def __init__(self, user, drink):
        self.user = user
        self.drink = drink

    def check(self):
        if self.user.balance < self.drink.price:
            return False

        return True
