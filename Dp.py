# Function to compute Fibonacci numbers using Dynamic Programming
def fibonacci(n):
    # Initialize a table to store Fibonacci numbers
    fib = [0] * (n + 1)
    fib[1] = 1  # Base case: fib(1) = 1

    # Fill the table from bottom-up
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# Driver code to test the function
if __name__ == "__main__":
    n = 10  # Find the 10th Fibonacci number
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is {result}")
