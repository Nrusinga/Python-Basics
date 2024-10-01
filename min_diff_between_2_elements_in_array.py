arr=[1,4,2,52,32,21,23,3,34]

arr.sort()

low=0
high=len(arr) - 1 
min=float('inf')
for i in range(len(arr)-1):
    if arr[i+1] - arr[i] < min:
        min=arr[i+1]-arr[i]
        min_pair = (arr[i], arr[i+1])

print("Pair with minimum difference:", min_pair)



