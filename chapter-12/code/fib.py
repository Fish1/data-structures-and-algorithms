
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

def fast_fib(n, memo = {}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    if not memo.get(n):
        memo[n] = fast_fib(n - 1, memo) + fast_fib(n - 2, memo)
        return memo.get(n)
    else:
        return memo.get(n)

for x in range(0, 50):
    print(fast_fib(x))
