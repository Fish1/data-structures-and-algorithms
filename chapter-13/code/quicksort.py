def quicksort(array):
    quicksort_r(array, 0, len(array) - 1)

# O(N * LOG(N))
def quicksort_r(array, start, stop):
    if start >= stop:
        return

    # O(N) 
    pivot = partition(array, start, stop)

    # O(N / 2)
    quicksort_r(array, 0, pivot - 1)
    # O(N / 2)
    quicksort_r(array, pivot + 1, stop)

# O(N)
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
quicksort(myarray)
print(myarray)
