arr=[1,2,2,3,2,2,4,5,5,5]
arr1=[]
""" for i in arr:
    count_i=0
    if i not in arr1:
        arr1.append(i)
    if i in arr1:
        
        count_i+=1
    print(f"{i} is ",count_i)

print(arr1) """
""" dict1={}
for i in range(len(arr)-1):
    count_i=0
    for j in range(len(arr)-1):
        if arr[i] == arr[j]:
            dict1[f'count_{i}']+=1

            print(count_i) """
dict1={}
val=2
for i in arr:
    if f'{i}' not in dict1:
        dict1[f'{i}'] = 1
    else:
        dict1[f'{i}'] += 1

for k,v in dict1.items():
    print(f"{k}:{v}")




        