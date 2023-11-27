# I forgot about f strings so paul helped me with that help

class Collectible(object):
    def __init__(self, d, c, v):
        self.description = d
        self.condition = c
        self.value = v
        

def collectible_printer(list_collectables):
    result_string = ""
    sum_value = 0

    for i in list_collectables:
        desc_each = i.description
        cond_each = i.condition
        sum_value += i.value
        result_string += f"{desc_each} in {cond_each} condition. "

    result_string += f"and the total value is {sum_value} dollars. "
    return result_string


box = Collectible("box", "used", 17)
wallet = Collectible("wallet", "good", 20)
Jordan1 = Collectible("Jordan 1", "used", 30)

collectibles_list = [box, wallet, Jordan1]

result = collectible_printer(collectibles_list)
print("Ms. Atwood has the following: ")
print(result)
