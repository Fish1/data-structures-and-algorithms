
def unique_paths(rows, columns, memo = {}):
    if rows == 1 or columns == 1:
        return 1

    if not memo.get((rows, columns)):
        memo[(rows, columns)] = unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)

    return memo[(rows, columns)]

print(unique_paths(3, 7))

