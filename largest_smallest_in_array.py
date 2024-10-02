arr=[63,54,98,34,89,2,18]
max=arr[0]
for i in arr:
    if i > max:
        max=i
print(max)

min=arr[0]
for i in arr:
    if i < min:
        min=i
print(min)

smallest=second_smallest=float('inf')  #very large valur 
largest=second_largest=float('-inf') #very small number 

for i in arr:
    if i < smallest:
        
        second_smallest=smallest
        smallest=i
    elif i < second_smallest and i != smallest:
        second_smallest=i

    if i > largest:
        
        second_largest=largest
        largest=i
    elif i > second_largest and i != largest:
        second_largest=i

print(smallest)
print(second_smallest)
print(largest)
print(second_largest)