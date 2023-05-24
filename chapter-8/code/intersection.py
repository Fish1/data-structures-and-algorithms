
def intersection(a1, a2):
    counts = {}

    for i in a1:
        curr = counts.get(i)
        if curr == None:
            counts[i] = 1


    for i in a2:
        curr = counts.get(i)
        if curr == 1:
            counts[i] = 2

    result = []
    for key, value in counts.items():
        if value == 2:
            result.append(key)

    return result

m1 = [1, 4, 9, 10, 22]
m2 = [4, 5, 10]

print(intersection(m1, m2))
    
