# Chapter 3 Notes

We've been counting the number of steps in previous chapters.

But that isn't very helpful because algorithms take different amounts of time base on the number of elemnts in the datasets they are run on.

An array with 22 elements will take 22 steps, an array with 100 elemnts might take 100 steps.

## Big O Notation
This is where big O notation comes into play.

We can say that a linear search will take O(N) steps. Where N is the number of elements in the data set.

Big O tells us how an alorithm will perform as a data set changes.

Take insertion into an array.
We know it takes one step. No matter how big the array grows it will always take 1 step.
We can say inerstion is O(1)

Linear search on the other hand takes N steps, where N is the number of elements.
O(N) or linear time.

We've seen binary search which grows 1 step as the data doubles
That will be O(log(N)) or logarithmic time.

