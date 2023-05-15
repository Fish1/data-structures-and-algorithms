
# O(N^2)
def greatestNumber_slow(array):
    for i in array:
        isIValTheGreatest = True

        for j in array:
            if j > i:
                isIValTheGreatest = False

        if isIValTheGreatest:
            return i

# O(N)
def greatestNumber_fast(array):
    greatest = array[0]
    for number in array:
        if number > greatest:
            greatest = number
    return greatest


my_array = [1, 5, 6, 2, 9, 3, 8, 4]
print(greatestNumber_slow(my_array))
print(greatestNumber_fast(my_array))
