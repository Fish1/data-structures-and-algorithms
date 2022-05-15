Notes:

Big O notation only concerns itself with general categories of efficiency.
  ex... O(1), O(N), O(N^2), O(logN) 

Selection sort takes half the time of bubble sort, but they are in the same O(N^2) category.

Big O cares about long-term efficiencies as the array grows. At some point, an O(N^2) algorithm will 
become slower than any O(N) algorithm.

Big O fails to classify algorithms that fall under the same category.


Exercises:

1) O(N) is the complexity of an algorithm that takes 4N+16 steps. We must drop all constants.

2) O(N^2) is the complexity of an algorithm that takes 2N^2 steps. The exponent describes the class
of the algorithm so we keep it.

3) O(N) is the complexity because the array is only iterated over 2N times. We drop the constant
to get the Big O notation.

4) For each element of the array, 3 steps are performed. Resulting in 3N steps. This can
be described as O(N) because we drop the constants.

5) O(N^2) describes the complexity because even though it only takes (N^2)/2 steps, the steps taken grow at an exponential rate.
