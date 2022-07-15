import numpy as np

# This is a recursive function that returns the maximum value in a list
# It is very slow because it is recursive
def slow_max(array):
  if len(array) == 1:
    return array[0]
  elif array[0] > slow_max(array[1:]):
    return array[0]
  else:
    return slow_max(array[1:])

# This is a recursive function that returns the maximum value in a list
# It is faster because it caches the results of the recursive calls
def fast_max(array):
  if len(array) == 1:
    return array[0]
  max_of_remainder = fast_max(array[1:])
  if array[0] > max_of_remainder:
    return array[0]
  else:
    return max_of_remainder

def loop_max(array):
  max = array[0]
  for number in array:
    if number > max:
      max = number
  return max

data = np.random.rand(10)
print(loop_max(data))
print(fast_max(data))
print(slow_max(data))