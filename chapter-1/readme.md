# Chapter 1

Data structures are responsible for storing data for our programs.

The most basic data structure might be considered the array. The computer will allocate a contiguous block of memory to store the data.

Common operations on data structures include...

1) Read
2) Search
3) Insert
4) Delete

In an array the computer can access a spot in an array instantly.

x = ['a', 'b', 'c']

y = x[2]

The computer can just stright to position 2 in memory and grab 'c'.

The computer might take n steps to search an array if the array has n elements. This is because we don't tell it where to go, we tell it what it needs to find.

If we tell it to search for 'b', the computer has no idea which index the 'b' element is at. So it must search the entire array starting at index 0.

It will increment until it finds element 'b'.

Insertion is interesting for an array. You might think it would be instant, but it is not.

x = [5, 2, 9, 4]

If we want to insert an elemnt at the end of the array it would be instant.

But if we want to insert an element at the second to last element, it will actually take 2 steps.
1) move the last element over to the right.
2) insert our new element

This will require more steps as we insert elements closer to the beginning.

In the worst case (when we insert at the first element), we need to perform n moves and 1 insert. (n being the number of elements in the array).

The same is true for deletes. If we delete an element we must shift all elements to the right of the deleted index, to the left.


Lets consider sets. It will change the rules for our inserts.

Read is still instant, search must still search all n elements, and deletes still shift the same.

But our insert now needs to perform extra logic. We need to verify, before we insert, that the element doesn't exist in the set already.

The insert must first check all elements in the set to verify it doesn't exist, if it doesn't, then shift elements to the right, then insert.

In the worst case of inserting at the beginning, we loop 1 time to verify, another loop to shift, then an insert.

2n + 1, steps are required to insert into a set.
