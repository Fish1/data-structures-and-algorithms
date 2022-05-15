### Notes

Big O notation only considers the highest order of N. 

**example:** O(N^2 + N) = O(N^2)

Selection sort takes N^2 / 2 steps in *all* cases.

Insert sort takes...

* N^2 steps in worst case
* N^2 / 2 steps in average case
* N steps in best case

Choosing between insert sort and selection sort depends on what assumptions we can make about our data.

### Exercises

1) 3N^2 + 2N + 1 steps results in an algorithm efficiency of O(N^2). We must drop constants and lower orders of N.

2) N + log(N) steps results in an algorithm efficiency of O(N) because log(N) is of a lower order than N.

3) 
* best case = 2; 
  The best case happens when the first and second items add up to 10.
* average case = N^2
  The average case happens when half way through checking, it finds two numbers that add up to 10.
* worst case = 2N^2
  The worst case happens when none of the values add up to 10, all combinations must be checked

Worst case big O is O(N^2)


4)
* best case = N
* average case = N 
* worst case = N

refer to answer4.go for revised code.

* best case = 1
* average case = N / 2
* worst case = N