# # nate helped me with returning what needed to be returned
#
# import random
#

def martinez_dictionary(characters):
    word_frequency = {}
    for char in characters:
        if char in word_frequency:
            word_frequency[char] += 1
        else:
            word_frequency[char] = 1
    return word_frequency
#
#
# def data_generator(char_names, len_list):
#     returned_list = []
#     for i in range(len_list):
#         returned_list.append(random.choice(char_names))
#     return returned_list
#
#
# with_data = data_generator(['Goku', 'Vegeta', 'Piccolo', 'Brolly'], 10)
#
# print(martinez_dictionary(with_data))
# print(martinez_dictionary(with_data))
# print(martinez_dictionary(with_data))

cities = {
    "Paris": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"],
    "New York": ["Statue of Liberty", "Central Park", "Empire State Building"]
}

city_name = "New York"
print(f"Landmarks in {city_name}: {', '.join(cities[city_name])}")
