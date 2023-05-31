def quickselect(array, k):
    quickselect_r(array, 0, len(array) - 1, k)

def quickselect_r(array, start, stop, search):
    if start >= stop:
        return
    # O(N) 
    pivot = partition(array, start, stop)

    if array[pivot] == search:
        print("Found {} at index {}".format(search, pivot))
        return

    # O(N / 2)
    quickselect_r(array, 0, pivot - 1, search)
    # O(N / 2)
    quickselect_r(array, pivot + 1, stop, search)

def partition(array, start, stop, search):
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
quickselect(myarray, 6)
