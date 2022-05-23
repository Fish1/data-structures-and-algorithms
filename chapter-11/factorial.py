def factorial(index):
  if index <= 1:
    return 1
  return index * factorial(index - 1)

def factorial_bottom(number, index = 1, product = 1):
  if index > number:
    return product
  return factorial_bottom(number, index + 1, product * index)

print(factorial(5))
print(factorial_bottom(5))
print(factorial(7))
print(factorial_bottom(7))
