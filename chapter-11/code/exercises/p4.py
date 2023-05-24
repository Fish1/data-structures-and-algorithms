
def index_x(str):
    if str[0] == 'x':
        return 0

    return 1 + index_x(str[1:])

mystr = 'aaaaaaxaaa'
print(index_x(mystr))
