nums = [2,20,4,10,3,4,5,19,18]

nums_up=sorted(nums)
print(nums_up)
nums_updated=[]


for i in range(len(nums_up)-1):
    if nums_up[i+1] - nums_up[i] == 1:
        if i not in nums_updated:
            
            nums_updated.append(nums_up[i])
        nums_updated.append(nums_up[i+1])
    
        
nums_updated=set(nums_updated)
print(nums_updated)
longest_streak=0
temp=[]
for i in nums_updated:
    if i-1 not in nums_updated:
        current_i=i
        current_seq=[current_i]

        while current_i + 1 in nums_updated:
            current_i +=1
            current_seq.append(current_i)
        if len(current_seq) > longest_streak:
            longest_streak=len(current_seq)
            temp=current_seq

print(temp)
    

