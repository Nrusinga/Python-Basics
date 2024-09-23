
def binary_search(arr,target):
    low=0
    high=len(arr)

    while low <= high:
        mid = (low + high)//2

        if (target < arr[mid]):
            high = mid - 1 
        elif (target > arr[mid]):
            low = mid + 1
        else:
            return mid 
        
    return -1
def binary_search_recursive(arr,low,high,target):
    

    while low <= high:
        mid = (low + high)//2

        if (target < arr[mid]):
            high = mid - 1 
            binary_search_recursive(arr,high,low,target)
        elif (target > arr[mid]):
            low = mid + 1
            binary_search_recursive(arr,high,low,target)
        else:
            return mid 
        
    return -1

numbers=[1,2,4,1,4,1,33,11,12]
numbers.sort()
x=binary_search(numbers,33)
y=binary_search_recursive(numbers,0,len(numbers)-1,33)
print(x)
print(y)
