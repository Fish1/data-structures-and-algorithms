1.1) Reading always takes one step.
1.2) We need to read all 100 elements to confirm that an element is not in an array.
1.3) 101 steps. 100 elements will be moved right, then one element is inserted at the beginning.
1.4) 1 step. Insertion at the end of an array always takes one step.
1.5) 100 steps. The first element gets deleted, then 99 elements need to be moved right.
1.6) 1 step. The last element gets deleted.

2.1) Reading from a set always takes one step.
2.2) We need to read all 100 elements to confirm that an element is not in an set.
2.3) 201 steps. First we need to read the entire set to confirm that the elements doesn't exist. Then all 100 elements need to be moved to the right. Then we can insert an element at the beginning of the set.
2.4) 101 steps. First we read the set to confirm the element doesn't exist. Then we can insert at the end.
2.5) 101 steps. Delete the first element, then move the 99 remaining elements to the left.
2.6) 1 step to delete from the last element of a set.

3) We need to search N elements. N being the size of the array to count every instance of "apple".
