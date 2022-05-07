def greatestNumber(array):
  for i in array:
    isIValTheGreatest = True
    for j in array:
      if j > i:
        isIValTheGreatest = False

    if isIValTheGreatest:
      return i

def greatestNumberFast(array):
  greatestValue = array[0]
  for value in array:
    if value > greatestValue:
      greatestValue = value
  return greatestValue 

print(greatestNumber([1,4,3,6]))
print(greatestNumberFast([1,4,3,6]))
