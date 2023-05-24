
def double_array(array, index = 0):
    if index >= len(array):
        return
    array[index] *= 2
    double_array(array, index + 1)


myarray = [1, 2, 3, 4, 5]

print(myarray)
double_array(myarray)
print(myarray)
