import random

class Coin:
    def __init__(self):
        self.__sideup = 'Heads'

    def get_sideup(self):
        return self.__sideup

    def toss(self):
        print('I am tossing the coin ... ')
        if (random.randint(0,1) == 0 ):
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
        print(self.__sideup)


count = 0
total = int(input('Enter the number of times to flip the coin: '))
for i in range(total):
    coin = Coin()
    coin.toss()
    if coin.get_sideup() == 'Heads':
        count += 1
print('Result : {} heads out of {}'.format(count, total))


