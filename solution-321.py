from enum import Enum

def get_input_as_float(label):
    input_value = None

    while type(input_value) != float:
        input_value = input(label)
        try:
            input_value = float(input_value)
            break
        except ValueError:
            continue

    return input_value

class Coin(Enum):
    PENNY   = 1
    NICKEL  = 5
    DIME    = 10
    QUARTER = 25

    def label(self, count):
        if self == Coin.PENNY:
            return "penny" if count == 1 else "pennies"
        if self == Coin.NICKEL:
            return "nickel" if count == 1 else "nickels"
        if self == Coin.DIME:
            return "dime" if count == 1 else "dimes"
        if self == Coin.QUARTER:
            return "quarter" if count == 1 else "quarters"

def change_due(price, amount_paid=1):

    coins = [Coin.QUARTER, Coin.DIME, Coin.NICKEL, Coin.PENNY]
    change = round(amount_paid - price, 2)

    print('Your change is: ')

    if change == 0:
        print(f'{0} {Coin.PENNY.label(0)}')
        return

    for coin in coins:
        coin_count = 0
        cents_value = round(coin.value / 100, 2)
        while change >= cents_value:
            coin_count += 1
            change = round(change - cents_value, 2)
        if coin_count > 0:
            print(f'{coin_count} {coin.label(coin_count)}')

def ex321():
    price = -1
    while price < 0 or price > 1:
        price = get_input_as_float('Enter a purchase price of a dollar or less: ')
    change_due(price)

ex321()