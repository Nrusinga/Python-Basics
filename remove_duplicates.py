arr=[1,4,2,5,5,2,3,1,4,1,4,5,2,3]

#arr_set=set(arr)
#print(arr_set)
arr_1=[]
for i in arr:
    if i not in arr_1:
        arr_1.append(i)

print(arr_1)


     