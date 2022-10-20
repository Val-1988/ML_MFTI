def almost_double_factorial(n):
    factorial = 1
    if n == 0:
        return 1
    elif n % 2 != 0:
        for i in range(n, -1, -2):
            factorial *= i
        return (factorial)
    elif n % 2 == 0:
        n = n-1
        for i in range(n, -1, -2):
            factorial *= i
        return (factorial)


print(almost_double_factorial(5))
print(almost_double_factorial(0))
print(almost_double_factorial(9))
print(almost_double_factorial(-2))
