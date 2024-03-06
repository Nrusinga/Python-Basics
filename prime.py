def isPrime(x):
    for i in range(2,x):
        if x%i == 0:
            print(f'{x} is not a prime number')
            break
    else:
        print(f'{x} is a prime number')







x=(int)(input("Enter a number:"))
if x > 1:
    isPrime(x)
else:
    print("Please enter a valid number!")