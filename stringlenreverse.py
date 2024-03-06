def lenString(str):
    count=0
    for i in str:
        count+=1
    return count
        
def reverseString(str):
    rev=''
    for i in str:
        rev=i+rev
    return rev
x=input("Enter the String")
print("The length of the string is: ",lenString(x))
print(f'Reverse of String {x} is:', reverseString(x))
