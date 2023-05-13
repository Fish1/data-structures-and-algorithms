
my_array = [1, 5, 9, 10]

def binary_search(array, search_value):
    length = len(array)
    index = length / 2
    check = array[index]

    while True:
        if length == 0:
            return None

        if check == search_value:
            return index

        if check < search_value:
            print("test")
            index -= length / 2
            length /= 2
        elif check > search_value:
            print("Binary Search!")
            index += length / 2
            length /= 2

binary_search(my_array, 10)

