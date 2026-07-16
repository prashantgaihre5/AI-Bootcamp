number = int(input("Enter a non-negative integer to find its factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0 or number == 1:
    print(f"The factorial of {number} is 1.")
else:
    result = 1
    for i in range(2, number + 1):
        result *= i
    print(f"The factorial of {number} is {result}.")
