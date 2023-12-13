def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
n = 10
result = [fibonacci_recursive(i) for i in range(n)]
print(result)