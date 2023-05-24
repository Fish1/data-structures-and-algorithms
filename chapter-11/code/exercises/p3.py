
def triangle_number(N):
    if N == 1:
        return 1

    return N + triangle_number(N - 1)

print(triangle_number(1))
print(triangle_number(2))
print(triangle_number(3))
print(triangle_number(4))
print(triangle_number(5))
print(triangle_number(6))
