
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)
n = 3
print(f'The Factorial of {n} is', factorial(n))

