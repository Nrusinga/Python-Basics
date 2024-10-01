arr=[5,7,4,3,9,8,19,21]
sum=12
""" l=[]
new_arr=[]
for i in arr:
    if i < sum:
        new_arr.append(i)

    for j in new_arr:
        if i + j == sum:
            l_i=[]
            l_i.extend([i,j])
            print(l_i)

print(new_arr) """
arr.sort()
low=0
high=len(arr)-1




while(low < high):
    
    if (arr[low] + arr[high]) == sum:
        print("Found pairs", arr[low], arr[high])
        high=high-1
        low=low+1
    elif (arr[low] + arr[high]) < sum:
        low=low+1
    else:
        high=high-1
    


