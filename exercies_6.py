#  Factorial 
def a(n):
    if n < 0:
        return "Invalid Entry."
    elif n == 0:
        return 1
    else:
        return n * a(n - 1)

number = int(input("Enter your number: "))

result = a(number)

print(f"The factorial of {number} is {result}")
