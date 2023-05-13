
my_array = [1, 5, 9, 10]

def linear_search(array, search_value):
    for index, value in enumerate(array):
        if value == search_value:
            return index
    return None

print(linear_search(my_array, 9))

print(linear_search(my_array, 5))

print(linear_search(my_array, 20))
