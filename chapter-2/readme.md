# Chapter 2 Notes

Algorithms are sets of instructions that are used to accomplish tasks.


### Ordered Arrays

Ordered arrays are just like the "classical" array. Except that the values in the data positions are positioned and ordered.

x = [1, 5, 6, 9]

If we want to insert data into an ordered array, we can no longer place it any where we want.

If we want to place 7 into x, we must insert it at position 3.

But the computer doesn't know that it needs to be at position 3, it must first calculate that.

Best case we can do an insert at the end, first check all N elements, then do the insert. And we don't have to shift any elements.


### Binary Search

For an array containing 100 elements, linear search will take at worst 100 steps.
Where a binary search will only need 7 steps.

If a binary search takes 7 steps for a 100 element array, then it will only take 8 steps for a 200 element array.

