
my_array = [3, 94, 1, 2, 9, 20, 1, 3, 9, 2, 3]

# worst case O(N^2) // when the array is backwards
# best case O(N) // when the array is sorted

# The number of operations can be described as...
# (N - 1) + (N - 2) + (N - 3) ... + 1
def bubble_sort(array):
    sorted = False 
    sort_until = len(array)
    while sorted == False:
        index = 1
        sorted = True
        while index < sort_until:
            prev = array[index - 1]
            curr = array[index]
            if prev > curr:
                array[index - 1], array[index] = array[index], array[index - 1]
                sorted = False
            index += 1
        sort_until -= 1

print(my_array)
bubble_sort(my_array)
print(my_array)
