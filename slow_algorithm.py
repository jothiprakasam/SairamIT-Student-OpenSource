# Task: Improve this slow algorithm to find the nth Fibonacci number.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Current implementation is very slow for large n.
# Contributors: Optimize this code to use a more efficient approach like memoization or iteration.

n = 35  # Test with a large number
print(f"Fibonacci({n}) =", fibonacci(n))
