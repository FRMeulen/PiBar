from datetime import datetime

class Logger:
    filePath = './res/Purchases.log'

    def log(self, user, drink):
        now = datetime.now().strftime('%d/%m/%Y %H:%M%S')
        with open(self.filePath, 'a') as logFile:
            logFile.write(f'[{now}] {user.name} purchased {drink.name} - Balance left: {user.balance}\n')
            
