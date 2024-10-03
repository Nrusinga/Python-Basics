s = "Was it a car or a cat I saw?"

s1=s.replace(" ","")
s2=s1.replace("?",'')
s4=s2.lower()
print(s4)
s3=''
for i in range((len(s4)-1),-1,-1):
    s3+=s4[i]
    
print(s3)

if s4 == s3:
    print("It's palindrome")
 
