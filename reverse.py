def reverse(x):
    rev=0
    sign = 1 if x >= 0 else -1
    x=abs(x)
    while(x!=0):
        rev= rev*10 + x%10
        x=x//10
        
    return rev*sign
    



x= int(input("Enter a number:"))
print(reverse(x))