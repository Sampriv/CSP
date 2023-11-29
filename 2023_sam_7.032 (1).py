class Flaherty(object):
    def __init__(self, name, wallet_value=0, possessions=None):
        self.name = name
        self.wallet_value = wallet_value
        self.possessions = possessions or []

    def earn(self):
        self.wallet_value += 30000
    
    def buy(self, item, cost):
        self.wallet_value -= cost
        self.possessions.append(item)
    
    def tweet(self):
        string = f"My name is {self.name} and I have {self.possessions}"
        return string


# Create two Flaherty objects
ned = Flaherty('Ned', 7739330, [])
juanita = Flaherty('Juanita', 320000, [])

# Call the earn method for the ned object
ned.earn()

# Call the buy method for the ned object with swapped names and items
ned.buy('food', 1273330)

# Call the tweet method for the ned object and print the result
print(ned.tweet())

# paul kim helped me with possessions=None and possessions or [] help
