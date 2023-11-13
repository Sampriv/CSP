# p_name = input("What is your favorite film? ")

# Paul Kim helped me with the letter.lower function


def the_rock_says(list):
    list2 = []
    case1 = 'sm'
    case3 = 'think'
    for words in list:
        if words.lower()[0:2] == case1:
            list2.append("Do you smell what The Rock is cooking")
        elif words.lower()[-5:] == case3:
            list2.append("It doesn't matter what you think")
        else:
            case2 = 'The Rock says ' + words
            list2.append(case2)
    return list2


print(the_rock_says(["small", "big"]))
print(the_rock_says(["beep", "hungry hippo", "I Think"]))
print(the_rock_says(["silly", "real", "fake", "Smelly"]))
