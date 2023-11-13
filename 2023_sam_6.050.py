def homework_times():
    """
    Creates some test data for this program.  Assumes 50 page of homework.
    Each homework takes between 1-20 minutes to complete
    :return: Returns a dictionary.  Key is the page of homework.  value is how long it takes to do that page (mins)
    """
    import random
    homework_dictionary = {}
    for i in range(50):
        homework_dictionary[i] = random.randint(1,20)
    return homework_dictionary


def split_dict_to_multiple(input_dict, friends):
    """Splits dict into multiple dicts with given maximum size.
    Returns a list of dictionaries."""
    import copy, math
    max_limit = math.ceil(50 / friends)
    chunks = []
    curr_dict ={}
    for k, v in input_dict.items():
        if len(curr_dict.keys()) < max_limit:
            curr_dict.update({k: v})
        else:
            chunks.append(copy.deepcopy(curr_dict))
            curr_dict = {k: v}
    # update last curr_dict
    chunks.append(curr_dict)
    return chunks
