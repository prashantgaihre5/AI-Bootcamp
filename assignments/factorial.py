def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    number = int(input("Enter a non-negative integer to find its factorial: "))
    fact = factorial(number)
    
    if fact is not None:
        print(f"The factorial of {number} is {fact}.")
    else:
        print("Factorial is not defined for negative numbers.")
