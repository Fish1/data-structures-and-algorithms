# Notes Chpater 5

### Selection Sort vs Bubble Sort

Selection and Bubble sort both perform O(N^2), but technically bubble sort performs O((1/2) N^2)

With big O notation we want to drop the contants.

This is because both algorithms grow exponentially.

O(N^2 / 2) = O(N^2)
O(2N) = O(N)

Big O is only about categorizing algoithms, not about finding their exact speed.

Both selection sort and bubble sort are in the same exponential category, even though selection sort is twice as fast.

We drop the constant because in the end, we only care about the alogrithms efficiency as N approches infinity.

Regardless of the constant, N^2 will always become greater than 1000N as N approches infinity.

We cannot use Big O to compare algorithms within the same class. We only compare alogithms of different classes.


