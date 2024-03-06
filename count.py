def count(x):
    count=0
    while(x>0):
        x=x//10
        count+=1
    return count


x= int(input("Enter the number:"))
print(count(x))
