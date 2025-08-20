memo = {}

def fib(n):
    if n in memo:
        return memo[n]

    if n == 1 or n == 2:
        memo[n] = 1
    else:
        memo[n] = fib(n-1) + fib(n-2)

    return memo[n]

def iter_fib(n):
    a = b = 1 
    c = a + b

    if(n==1 or n == 2):
        return 1 

    for cnt in range(3, n+1):
        c = a+b
        a = b
        b = c 

    return c

print(fib(8))
print(iter_fib(8))

def dp_arr_fib(n):
    arr = [1] * (n+1)

    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]

    return arr[n]

print(dp_arr_fib(8))

def fib(n: int) -> int:
    """Return nth Fibonacci number in O(log n) time using fast doubling."""
    if n < 0:
        raise ValueError("Input must be non-negative")

    def _fib(k):
        if k == 0:
            return (0, 1)
        a, b = _fib(k >> 1)   # divide n by 2
        c = a * (2 * b - a)
        d = a * a + b * b
        if k & 1:  # if k is odd
            return (d, c + d)
        else:      # if k is even
            return (c, d)

    return _fib(n)[0]


# Example usage
for i in range(10):
    print(f"F({i}) = {fib(i)}")
