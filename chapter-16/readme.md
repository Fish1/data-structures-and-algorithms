# Chapter 16 Notes

## Priority Queues

A priority queue is a queue. But instead of FIFO, the items with the highest "severity" go out first.

A priority queue is an abstact data structure, which is built on top of a more fundamental data structure.

We could implement a priority queue with an ordered array.

After an item is inserted into the array, we would need to perform a sort function on the entire array, and then pull from the front.

For a priority queue, deletion is O(1) because we always delete the first element in one step.
For insertion, the operation would take O(N) because we would need to iterate over the sorted array to see where the item should be inserted at, then move the remaining items over.

## Binary heap

Because insertion into an ordered array is O(N) we can use a binary heap to make it faster.

Rules of the binary heap

1. The value of each node must be greater than each of its descendant nodes.
2. The tree must be complete.
