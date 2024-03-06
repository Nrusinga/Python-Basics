def perfectNum(x):
    sum=0
    for i in range(1, (x//2)+1):
        if x % i == 0:
            sum += i
    if sum==x:
        return True
    else:
        return False




x=int(input('Enter the number:'))
print(perfectNum(x))