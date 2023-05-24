
def factorial(number):
    if number <= 2:
        return number
    return number * factorial(number - 1)

print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
