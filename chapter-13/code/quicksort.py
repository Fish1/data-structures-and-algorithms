
def quicksort(array, start, stop):
    if len(array) <= 1 or start >= stop:
        return

    print(array, start, stop)
    center = partition(array, start, stop)
    
    quicksort(array, 0, center)
    quicksort(array, center + 1, stop)
    
def partition(array, start, stop):
    pivot = stop
    left = start
    right = pivot - 1
    while True:
        while array[left] < array[pivot]:
            left += 1

        while array[right] > array[pivot] and right > start:
            right -= 1

        if left >= right:
            array[pivot], array[left] = array[left], array[pivot]
            return left
        else:
            array[left], array[right] = array[right], array[left]


myarray = [0,5,2,1,6,3]
quicksort(myarray, 0, len(myarray) - 1)
print(myarray)

