data = [1, 4, 2, 5]

def double_array(arr, index = 0):

  # base case when index >= length of data
  if index >= len(arr):
    return

  # double the current index
  arr[index] = arr[index] * 2

  # increment
  double_array(arr, index + 1)


print(data)
double_array(data)
print(data)
