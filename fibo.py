def fibonacci_series(n):
    a, b = 0, 1
    count = 0
    series = []
    while count < n:
        series.append(a)
        a, b = b, a + b
        count += 1
    return series

# Get the first 10 numbers of the Fibonacci series
fib_numbers = fibonacci_series(10)

# Print the series
print("Fibonacci Series (first 10 numbers):")
for num in fib_numbers:
    print(num)
