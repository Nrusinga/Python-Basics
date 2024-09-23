

def find(numbers):
    duplicates=[]
    for i in range(len(numbers)):
        for j in range(i+1 , len(numbers)):
            if(numbers[i] == numbers[j] and numbers[i] not in duplicates):
                duplicates.append(numbers[i])
                #print( "{} is a duplicate".format(numbers[i]))
                break
    return duplicates
numbers=[3,2,1,3,3,4,2,4,4]
x=find(numbers)
print(x)