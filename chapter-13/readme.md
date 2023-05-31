# Chapter 13 Notes

## Recursive Algorithms for Speed

Recursion unlocks new algorithms, including algorithms that can be much faster. 

One very fast recursive algorithm is quicksort.

Quick sort speed
Best: O(N log(N))
Average: O(N log(N))
Worst: O(N^2)

Average case happens when the pivot falls in the middle
of the array. This happens when its evenly mixed.

XXXXXXXX
XXXX XXXX
XX XX XX XX
X X X X X X X X

Worst case happens when the pivot falls at the beginning or 
end of the array. This is when is reverse or forward sorted.

XXXXXXXX
X XXXXXXX
XX XXXXXX
XXX XXXXX
XXXX XXXX
XXXXX XXX
XXXXXX XX
XXXXXXX X
XXXXXXXX
