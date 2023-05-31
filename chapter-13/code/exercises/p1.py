
# quick sort the array
# then pick the top 3 elements
# O (N * LOG(N))
# because quicksort is O(N * LOG(N))

myarray = [0,5,2,1,6,3]
myarray.sort()
x = myarray[-1]
y = myarray[-2]
z = myarray[-3]
print(x * y * z)

