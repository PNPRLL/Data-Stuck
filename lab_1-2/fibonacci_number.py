"""Fibonacci"""
def fibonacci(n):
    """Start"""
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive Case: เรียกตัวเองซ้ำตามสูตร F(n-1) + F(n-2)
    return fibonacci(n-1) + fibonacci(n-2)

num = int(input())
print(fibonacci(num))
