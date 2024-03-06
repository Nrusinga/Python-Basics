def factorial(x):
    fact=1
    while(x!=0):
        fact=fact*x
        x-=1
    return fact


def factorial_recursive(x):
    fact=1
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x * factorial_recursive(x-1)

x=int(input("Enter the number"))
print(f"The factorial of the number {x} is", factorial(x))
print(f"The factorial of the number {x} is", factorial_recursive(x))
