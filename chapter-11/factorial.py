def factorial(index):
  if index <= 1:
    return 1
  return index * factorial(index - 1)

print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))