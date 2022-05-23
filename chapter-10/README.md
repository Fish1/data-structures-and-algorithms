### Notes

Recursion is when a function calls itself. Though, to be usefull, recusive function must be carefully crafted.

Each time a recursive function is called, it adds another layer to the "call stack" or just the "stack". When one of the calls hits a return, it starts to pop functions off the call stack, and propogates up.

Some functions can are more clearly written as recursive functions, especially in situations where you have an undefined numbers of layers of data. For example, a filesystem and directory traversal.

### Excercises

1) The base case is low=12 and high=10. This will result in the recursive function propogating up.

2) This change will result in an infinite recursive function and a stack overflow. This is because the basecase of n=1 will never be hit.

3) The basecase must return 0 when high is less than low. Refer to answer3.go for the code.

4) Refer to answer4.py