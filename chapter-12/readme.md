# Chapter 11 Notes

Recurssive algorithms tend to have poor performance.

We can use some techniques to speed them up.

Having multiple recurssive calls to the function, tends to result in poor performance.

Try to use only a single recurssive call where possible.

## Overlapping Sub Problems

Take the fib problem.

We have Fib(n) = Fib(n - 1) + Fib(n - 2)

We can see to calculate Fib(n - 1) we need to calculate Fib(n - 2)

But now we are calculating Fib(n - 2) twice.



