
def count_characters(arr):
    if len(arr) == 0:
        return 0
    return len(arr[0]) + count_characters(arr[1:])

mydata = ["ab", "c", "def", "ghij"]

print(count_characters(mydata))
