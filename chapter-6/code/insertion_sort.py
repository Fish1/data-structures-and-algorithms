
my_array = [4, 5, 9, 3, 2, 5, 6, 3]
my_array_2 = [8, 4, 2, 3]

def insertion_sort(array):
    for right_index in range(1, len(array)):
        gap_index = right_index
        right_value = array[right_index]
        for left_index in reversed(range(0, right_index)):
            left_value = array[left_index]
            if left_value >= right_value:
                array[gap_index] = left_value
                gap_index = left_index
            else:
                break
        array[gap_index] = right_value

print("Unsorted:", my_array)
insertion_sort(my_array)
print("Sorted:", my_array)

print()

print("Unsorted:", my_array_2)
insertion_sort(my_array_2)
print("Sorted:", my_array_2)
