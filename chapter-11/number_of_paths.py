def number_of_paths(n):
  if n < 0:
    return 0
  elif n == 0 or n == 1:
    return 1
  return number_of_paths(n - 1) + number_of_paths(n - 2) + number_of_paths(n - 3)

print(number_of_paths(5))
