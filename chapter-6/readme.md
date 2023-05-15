# Notes Chpater 6

Normally we look at how many steps an algorith takes in the worst case.

But we can also look at the best case or average case.

In big O we can drop anything that isn't the largest exponent

O(N^2 + N) = O(N^2)

as N approaches infinity, the N part becomes insignificant...

Insertion sort:
Worst case = O(N^2)
Average case = O(N^2 / 2)
Best case = O(N)

Selection Sort
Worst case = O(N^2 / 2)
Average case = O(N^2 / 2)
Best case =  O(N^2 / 2)

With this comparison we need to make a desision, if our data is mostly sorted, then insertion sort might be good.

If our data is never sorted or often reversed, then we can choose selection sort.


