def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y  

num1 = int(input("Enter a number: "))
num2 = int(input("Enter the second number: "))


print("The sum of these numbers is:", add(num1, num2))
print("The difference of these numbers is:", sub(num1, num2))
print("The product of these numbers is:", multiplication(num1, num2))
print("The quotient of these numbers is:", division(num1, num2))
