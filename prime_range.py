def primeNos(firstNumber,secondNumber):
    for i in range(firstNumber,secondNumber):
        for j in range(2,i):
            if (i%j == 0):
                break
        else:
            print(i, "is a prime number")






firstNumber=int(input("Enter the first number:"))
secondNumber=int(input("Enter the second number:"))
if ( firstNumber > secondNumber ) | ( firstNumber < 1) | ( secondNumber < 1):
    print("Please enter a valid range")
else:
    primeNos(firstNumber,secondNumber)