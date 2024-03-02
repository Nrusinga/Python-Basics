
'''def fibonacci(index):
    temp=0
    first=0
    second=1
    print(first)
    print(second)
    for i in range(0,index):
        temp=first+second
        first=second
        second=temp
        print(temp)
        

index=int(input("Enter the value of the index:"))

fibonacci(index)'''


def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-2) + fibonacci(i-1)
        
i = int(input('Enter the value of i:'))
for i in range(0,i):
    print(fibonacci(i))

    