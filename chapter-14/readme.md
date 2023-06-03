# Notes Chapter 14

## Node Based Data Structures

Nodes are bits of data that can be distributed across memory. Generally they link to one another.

## Linked List

The simples node-based data structure is the linked list. It looks like an array but has specific properties that you should consider when deciding to use one.

Linked lists are not contiguous blocks of memory, its memory is scattered across the system in these nodes.

In a linked list, the nodes will contain a pointer to the next node.

The head node, is the first node. The tail node is the last node.

Linked lists might not seem faster than arrays...
Read O(N)
Search O(N)
Insert O(N)
Delete O(N)

But that are faster with insert and delete in some cases. That case being when we want to go through the list and delete many elements.

If we had a list of all numbers, and we wanted to delete even ones. We simply iterate over the list and change the pointers.

With an array, we would need to delete elements, and perform large shifting operations.
