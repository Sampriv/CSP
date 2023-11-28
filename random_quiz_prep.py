#guess = input("Give me an integer between 1 and 10 ")
#if guess < str(10):
#  print("Your number is less than 10")
#else:
#   print("Your number is greater than or equal to 10")

#q1 = input ('What is your favorite color? ')
#if q1 == 'red':
#    print('You like red, Bleah')
#elif q1 == 'blue':
#    print('You like blue, gross')
#elif q1 == 'yellow':
#    print('pee is yellow')
#else:
#    print('Nice color')

#grocery1 = 'banana'
#grocery2 = 'apple'
#grocery3 = 'strawberry'
#pick = input("Gimme a grocery number 1-3 ")
#pick = int(pick)
#you = "you selected "
#if pick == 1:
#   print(you + grocery1)
#elif pick == 2:
#   print(you + grocery2)
#elif pick == 3:
#   print(you + grocery3)
#else:
#   print("Pick between 1-4")

#name = "Kann"

#if name == "Wu":
#   print("Dr. Wu is OK")
#elif name == "Kann":
#   print("Mr. Kann is the baddest baddass of all time")
#else:
#   print("who?")

#q1 = input('hello! What is your favorite youtube channel? ')
#if q1 == 'pewdiepie':
#    print('That is a famous youtuber')
#elif q1 == '360jeezy':
#    print('You must like barbering!')
#elif q1 == 'cocomelon':
#    print('My little brother and sister like that one too!')
#elif q1 == 'Ryans toys review':
#    print('I have not heard of that one')

#pick = input("Give me an integer between 1 and 4 ")
#pick = int(pick)
#groceries = ['banana', 'apple', 'strawberry', 'bread']
#print("You selected this grocery: " + groceries[pick-1])

#def groceries():
#    groceries = ['banana', 'apple', 'strawberry', 'bread']
#    pick = input("Gimme a grocery number 1-4 ")
#    pick = int(pick)
#    you = "you selected "
#    print(you + groceries[pick - 1])
#    if pick > 4:
#        print('Please pick a number between 1-4')

#import random

# rsta_cs_teachers = ['Wu', 'Martinez', 'Atwood']
# how_long = len(rsta_cs_teachers)
# number = random.randint(0,len(rsta_cs_teachers)-1)
# teacher = rsta_cs_teachers[number]
# print("My favorite RSTA CS teacher is this person: " + teacher)

#import random
#list = ['no', 'yes', 'maybe', 'in the future']
#question = input('ask the fortune teller a question')
#number = random.randint(0,len(list)-1)
#print(list[number])

# Rewrite the following code using lists and explain why it is better with lists than with individual variables:
# grocery1 = 'banana'
# grocery2 = 'apple'
# grocery3 = 'strawberry'
# pick = input("Gimme a grocery number 1-3 ")
# you = "you selected "
# if pick == '1':
#    print(you + grocery1)
# elif pick == '2':
#    print(you + grocery2)
# if pick == '3':
#    print(you + grocery3)
# else:
#    print("Pick between 1-4")

# import random=
# fruits = ['banana', 'apple', 'strawberry']
# number = random.randint(0,len(fruits)-1)
# fruitstuff = fruits[number]
# print('you get a ' + fruitstuff)

# GAME SHOW BELOW 3.020

# Function to select and print a random prize from the list
# def select_game_show_prize(prizes):
#     selected_prize = random.randint(0, len(prizes) - 1)
#     print("Congratulations! You've won:", prizes[selected_prize])

# LILO HACKER BELOW 4.013

# def seven_counter(input_string):
#     count_sevens = 0
#     for digit in input_string:
#         if digit == '7':
#             count_sevens += 1
#     if count_sevens > 3:
#         return "Lucky"
#     else:
#         return "Unlucky"

# Testing the function
# input_strings = ["123777", "777777", "456789"]

# for string in input_strings:
#     result = seven_counter(string)
#     print(f"Input: {string}, Result: {result}")

# # Function to count vowels in a word
# def vowel_counter(word):
#     vowels = "aeiou"
#     count = 0
#     for char in word:
#         if char.lower() in vowels:
#             count += 1
#     return count

## 4.021 BELOW TTHE ROCK

# # Function to filter words over 5 characters long, excluding 'quit'
# def over_five(word_list):
#     result = []
#     for word in word_list:
#         if word == 'quit':
#             return []  # Return blank list if 'quit' is encountered
#         elif len(word) > 5:
#             result.append(word)
#     return result

# Fortune teller:  Write a 4-8 line program that does this:

# Ask the fortune teller a question Should I eat this vegan cake
# Fortune teller says this: no
# Ask the fortune teller a question Should I go to school today
# Fortune teller says this: let me think about it
# Ask the fortune teller a question Are you even listening to me
# Fortune teller says this: yes
# Ask the fortune teller a question How do u talk without a mouth
# Fortune teller says this: no
# `
# In this program you need the following elements:
# Random number
# A list of at 4-5 “fortunes”
# Ask the user a question

# rsta_cs_teachers = ['Wu', 'Martinez', 'Atwood']
# how_long = len(rsta_cs_teachers)
# number = random.randint(0,len(rsta_cs_teachers)-1)
# teacher = rsta_cs_teachers[number]
# print("My favorite RSTA CS teacher is this person: " + teacher)

#3.027 BELOW

# minimum
# Create a function minimum
# Input parameter: A list of integers
# Returns: The minimum integer in the list (integer)

# Call the function 3x in the main code to test it.

# def minimum(list):
#     min = list[0]
#     for num in list:
#         if num < min:
#             min = num
#     return min
# print(minimum([3, 5, 4, 2, 1, 3,]))


# def add_assignment(p_dict, category, grade):
#     if category in p_dict.keys():
#         p_dict[category].append(grade)
#     else:
#         p_dict[category] = [grade]
#     return p_dict


# dict = {}
# dict = add_assignment(dict, "tests", 100)
# print(dict)
# dict = add_assignment(dict, "homework", 100)
# print(dict)
# dict = add_assignment(dict, "labs", 30)
# print(dict)


# def calculate_grade(dict):
#     total_grade = 0
#     if "homework" in dict.keys():
#         homework_avg = sum(dict['homework']) / len(dict['homework'])
#         total_grade += homework_avg * 0.2
#     if "tests" in dict.keys():

#         test_avg = sum(dict['tests']) / len(dict['tests'])
#         total_grade += test_avg * 0.3

#     if "labs" in dict.keys():

#         lab_avg = sum(dict['labs']) / len(dict['labs'])
#         total_grade += lab_avg * 0.5

#     return total_grade


# calculate_grade(dict)

# final_grade = calculate_grade(dict)
# print(final_grade)
#sam gave me help on creating the calculate grade function

# def item_list_to_dictionary(items_sold):
#     items_sold_dict = {}
#     for i in items_sold:
#         if i in items_sold_dict:
#             items_sold_dict[i] += 1
#         else:
#             items_sold_dict[i] = 1
#     return items_sold_dict


# sold = item_list_to_dictionary


# def min_item(sales_dict):
#     if not sales_dict:
#         return None
#     min_key = min(sales_dict, key=sales_dict.get)
#     return min_key


# items_sold = ['meatsa pizza', 'chicken parm', 'noodles noodles', 'meatsa pizza', 'chicken parm',
#               'noodles noodles', 'chicken parm', 'tiramisu', 'garlic bread', 'eggplant parm',
#               'noodles noodles', 'spaghetti tacos', 'garlic bread', 'meatsa pizza']

# sales_dict = item_list_to_dictionary(items_sold)
# print("Original Dictionary:", sales_dict)

# for i in range(5):
#     min_key = min_item(sales_dict)
#     del sales_dict[min_key]

# print("Dictionary after removing 5 lowest selling items:", sales_dict)







# 6.011
# Point out the dictionary, keys, and values in this code:

# scores = {'Jojo': 200,
#             'Abel': 300,
#             'Gwynneth': 250}

# keys are Jojo, able and gwynneth
# the values are 200, 300, and 250

# Debug this code: 

# scores = {'jojo': 200,
#         'Abel': 300,
#         'Gwynneth': 250}
# print(scores['jojo'])

# ^
# #put squigglies instead of square brackets for the dictionary


# Debug this code: 

# scores = {'Jojo': 200,
#           'Abel': 300,
#           'Gwynneth': 250}
# if 'Jojo' in scores.keys():
# print("Yes! There is a person named Jojo with a score of 200")

# change keys to values and correct from strings to integer


# # Debug this code: 
# scores = {'jojo': 200,
#             'Abel': 300,
#             'Gwynneth': 250}
# print(scores['jojo'])
#                  {'jojo' in scores.keys}


# Debug this code: 

# scores = {'jojo', 200,
#            'Abel', 300,
#            'Gwynneth', 250}
# print(scores[jojo])
# ^ change commas with colons and change jojo to 'jojo'


# Explain why this code doesn’t work: This code does not work because 200 is not a key it is a value, to make this code be correct it would be if "Jojo" in scores.keys():

# scores = {'Jojo': 200,
#           'Abel': 300,
#           'Gwynneth': 250}
# if 200 in scores.keys():
#     print("Yes! There is a person named Jojo with a score of 200")




# # Given this dictionary, write a code that checks if “Abel” is present in the dictionary as a key 

# scores = {'Jojo': 200,
#           'Abel': 300,
#           'Gwynneth': 250}
# if 'Abel' in scores.keys():
#     print('Yes! There is a person named Abel with a score of 300')

#------------------------------------------------------------------------------------------------


#6.022


# These oopses are common things that folks mess up on.  Debug the following programs:

# #I want to add 100 points to jojo’s score
# scores = {'jojo': 200,
#          'Abel': 300,
#         'Gwynneth': 250}


# scores['jojo'] = 100

# ^ += 100 instead of = 100





# # I want to add 100 points to jojo’s score
# scores = {'jojo': 200,
#          'Abel': 300,
#          'Gwynneth': 250}


# scores[jojo] += 100
# ^ put jojo in ''


# If the name isn’t in the dictionary, I want to add it as a key with the score specified.
# scores = {'jojo': 200,
#           'Abel': 300,
#           'Gwynneth': 250}


# joses_score = 100
# name = 'Jose'
# if name not in scores.keys():
#    dictionary[key] = value

# print(scores)

# ^ change dictionary too scores. change [key] to name. change value to joses_score


# def vote_counter(voted_list):
#     voted_dict = {}
#     for name in voted_list:
#         if name in voted_dict:
#             voted_dict[name] += 1
#         else:
#             voted_dict[name] = 1
#     return voted_dict




# def vote_counter(voted_list):
# voted_dict = {}
# for name in voted_list:
#     if name in voted_dict:
#         voted_dict[name] += 1
#     else:
#         voted_dict[name] = 1
# return voted_dict



# def vote_counter(voted_list):
# voted_dict = {}
# for name in voted_list:
#     if name in voted_dict:
#         voted_dict[name] += 1
#     else:
#         voted_dict[name] = 1
# return voted_dict



# def vote_counter(voted_list):
# voted_dict = {}
# for name in voted_list:
#     if name in voted_dict:
#         voted_dict[name] += 1
#     else:
#         voted_dict[name] = 1
# return voted_dict



 #dictionary with keys people who were voted for and values the number of votes recieved


# a = vote_counter(['Luz', 'Luz', 'Luz', 'Rajiv', 'Rajiv', 'Random', 'Random'])
# print(a)




# Create a function vote_counter
# Input parameter: A list of people who received votes (i.e. [‘Luz’, ‘Rajiv’’, ‘Rajiv’, ‘Rajiv’, ‘Luz’, ‘Finn’’]
# Returns: dictionary with keys people who were voted for and values the number of votes received (i.e. {‘Luz’: 2, ‘Rajiv’: 3, ‘Finn’:1}
# Call the function 3x in the main code to test it.


#-------------------------------------------------------------------------------------------


#6.032

    # dictionary keeps track of what I eat for breakfast, lunch, and dinner.  Values are LISTS. Two mistakes in this one.


# meals = {}
# meals['breakfast'] = ['orange']
# meals['breakfast'].append('banana')

# print(meals)

# you have to first make a list and then append tio that list

# Print the LAST thing I ate for breakfast.  One bug.


# meals = {}
# meals['breakfast'] = ['brains', 'brains', 'brains', 'guts']
# print(meals['breakfast'][-1])
#add square brackets at the end with -1 to find the last thing in the list


# Prints everything I ate for lunch on different line.  
# meals = {}
# meals['breakfast'] = ['brains', 'brains', 'brains', 'guts']
# for meal in meals['breakfast']:
#      print(meal)



# # Create a function first_value
# # Input parameters:  
# # A dictionary.  Keys are strings, values are LISTS of integers 
# # A string that says what key you are looking for (string)
# # Output:
# # A string:
# # If the key is in the dictionary, return the FIRST item of the value (remember, values are lists)
# # If the key is not in the dictionary, return “not in dictionary”
# # In the main part of the code, write a test case for this function

# # Same as previous, but this time, I want to change the first value in each list to be zero.


# def first_value(p_dict, p_string):
#     if p_string in p_dict:
#         return p_dict[p_string][0]
#     else:
#         return "not in dictionary"
#             # Testing the function
# test_dict = {'apple': [10, 2, 3, 4, 5], 'orange': [1, 52, 345, 1], 'banana': [1, 25, 2, 2, 5]}
# test_key = 'apple'
# result = first_value(test_dict, test_key)
# print(result)

# Same as previous, but this time, I want to change the first value in each list to be zero.


# def first_value(p_dict, p_string):
#     if p_string in p_dict:
#         p_dict[p_string][0] = 0
#         return p_dict[p_string][0]
#     else:
#         return "not in dictionary"
#             # Testing the function
# test_dict = {'apple': [10, 2, 3, 4, 5], 'orange': [1, 52, 345, 1], 'banana': [1, 25, 2, 2, 5]}
# test_key = 'orange'
# result = first_value(test_dict, test_key)
# print(result)

# This code is supposed to print out the species we find in the school, but does not.

# species = {"Martinez": "Human", "Tupper": "Human", "Wu": "Martian", "Hauck": "Rhino"}
# for value in species.values():
#    print("Here is a species we have in school!" + str(value))
#     ^add .values(): after species to get the value of the key and not the key

# This function is supposed to return the maximum number of children that one of these teachers has.  But it crashes.

# def blah():
#    number_of_children = {"Martinez": 1, "Tupper":2, "Wu": 2, "Hauck": 8}
#    max_person = ''
#    max_children = number_of_children[0]
#    for key in number_of_children:
#           if number_of_children[key] > max_children:
#               max_children = number_of_children[key]
#    return max_children

# print(blah())
#^Change number of children[0] to -1 because u have to set the value to a number


#HAVENT FINISHED ANYTHING UNDER THIS
# ----------------------------------
# def max_key(p_dict):
# max = 0
#     if value in random_dict.value is > max:
#         value = max

# random_dict = {'abc': 1, 'abcd': 2}
#     return #key with mawimum value in the dictionary(string)



# Create a function max_key
# Input parameters:  
# A dictionary.  Keys are strings, values are integers 
# Returns:
# The KEY with the maximum value in the dictionary (string)
# In the main part of the code, call max_key to find the value with the maximum key
# Delete the key/value pair in the dictionary that has the maximum value.  You have not done this; Googling is part of the quiz.  https://thispointer.com/different-ways-to-remove-a-key-from-dictionary-in-python/

# Create a function even_values
# Input parameters:  
# A dictionary.  Keys are strings, values are integers 
# Returns:
# A dictionary with value from the original dictionary, but ONLY if the value is even.

# I have a dictionary with keys that are strings (colleges) and values that are integers (scores).  How do I convert this key to 2 lists, one of colleges and one of scores?  
# Debug, find the error.  These are all classic errors that folks make in this lab.  All fixes are 1 line only.l









