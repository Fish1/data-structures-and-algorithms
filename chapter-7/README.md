### Exercises 

1) The number of steps required to complete this algorithm is 3N / 2. The array loops from the start to middle of the array, and each iteration does 3 steps. O(3N/2) reduces to O(N).

2) This algorithm combines the two unrelated datasets. So the number of steps required is N + M. N being the length of the first array and M being the length of the second. Our big O notation reduces to O(N)

3) This algorithm loops through two different datasets. First it loops through the haystack N times, and for each N it loops through the needle M times. Resulting in a complexity of O(N*M). This describes a range of efficiencies between O(N) when M is 1 and O(N^2) when M is N.

4) This algorithm will loop through the array 3 times for each product. But since previous checked values no long need to be checked on each iteration we can reduce the number of steps. The inner most iteration takes N / 4 steps, middle iteration takes N / 2 steps and the outermost takes N step; N * (N/2) * (N/4) = (N^3) / 8. This reduces to O(N^3).

5) This algorithm will eliminate half of the result in every step. Resulting in an efficiency of O(log(n)).