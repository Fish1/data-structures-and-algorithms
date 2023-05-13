from math import floor

my_array = [1, 5, 9, 10]

def binary_search(array, search_value):
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:
        index = floor((right_index + left_index) / 2)
        value = array[index]

        if value == search_value:
            return index

        if value > search_value:
            right_index = index - 1
        else:
            left_index = index + 1

    return None


index = binary_search(my_array, 10)
print(index)

