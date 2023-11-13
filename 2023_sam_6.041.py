def item_list_to_dictionary(items_sold):
    items_sold_dict = {}
    for i in items_sold:
        if i in items_sold_dict:
            items_sold_dict[i] += 1
        else:
            items_sold_dict[i] = 1
    return items_sold_dict


sold = item_list_to_dictionary


def min_item(sales_dict):
    if not sales_dict:
        return None
    min_key = min(sales_dict, key=sales_dict.get)
    return min_key


items_sold = ['meatsa pizza', 'chicken parm', 'noodles noodles', 'meatsa pizza', 'chicken parm',
              'noodles noodles', 'chicken parm', 'tiramisu', 'garlic bread', 'eggplant parm',
              'noodles noodles', 'spaghetti tacos', 'garlic bread', 'meatsa pizza',
              'eggplant parm', 'salad with italian dressing']

sales_dict = item_list_to_dictionary(items_sold)
print("Original Dictionary:", sales_dict)

for i in range(5):
    min_key = min_item(sales_dict)
    del sales_dict[min_key]

print("Dictionary after removing 5 lowest selling items:", sales_dict)
