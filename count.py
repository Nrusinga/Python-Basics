def count(x):
    while(x>0):
        x=x//10
        count+=1
    return count








x= input("Enter the number:")
print(count(x))