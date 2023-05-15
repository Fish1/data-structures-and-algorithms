my_array = [4, 5, 9, 3, 2, 5, 6, 3]

# O(N^2)
# you can see it loop over all the elements in the array twice
def selection_sort(array):
    for (left_index, left_value) in enumerate(array):
        lowest_index = left_index
        lowest_value = left_value

        for (right_index, right_value) in enumerate(array[left_index + 1:]):
            if right_value < lowest_value:
                lowest_index = right_index + left_index + 1
                lowest_value = right_value

        array[left_index] = lowest_value
        array[lowest_index] = left_value

print(my_array)
selection_sort(my_array)
print(my_array)
