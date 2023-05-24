
def add_until_100(array):
    if len(array) == 0:
        return 0

    subanswer = add_until_100(array[1:])

    if array[0] + subanswer > 100:
        return subanswer
    else:
        return array[0] + subanswer

myarray = [1, 3, 4, 20, 2, 2, 2, 57, 8, 15]
print(add_until_100(myarray))
