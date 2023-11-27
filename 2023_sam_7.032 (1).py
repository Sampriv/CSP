from os import name


class Flaherty(object):
    def __init__(self, name, wallet_value, possessions):
        self.name = name
        self.wallet_value = wallet_value
        self.possessions = possessions

def earn(wallet_value):
    wallet_value += 30000
    
def buy(wallet_value, possessions, item, cost):
    wallet_value -= cost
    possessions.append(item)
    
def tweet(wallet_value, possessions):
    string = f"My name is {name} and I have {possessions}"
    

    