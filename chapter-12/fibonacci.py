def fib(n, memo):
    if n == 0 or n == 1:
        return n
    if n in memo:
      return memo[n]
    memo[n] = fib(n-2, memo) + fib(n-1, memo)
    return memo[n]

for i in range(400):
    print(fib(i, {}))