
def reverse_string(str):
    if len(str) == 1:
        return str[0]
    return reverse_string(str[1:]) + str[0]

mystr = "abcdef"
print(mystr)
print(reverse_string(mystr))
