def collectvalues(x):
    for i in range(0,x):
        ele=float(input())
        l1.append(ele)
        
def average(l1):
    tot=0
    for i in range(0,len(l1)):
        tot=tot+l1[i]
    print(tot)
    return tot/len(l1)
        
    
    
    
    
    

l1=[] 
x=int(input("Enter number of elements:"))
collectvalues(x)
print(average(l1))