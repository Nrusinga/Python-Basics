x='charan'
y='rakesh'
res=''
res1=''
for i in range(len(x)):
    if x[i] not in res:
        res+=x[i]
for i in range(len(y)):
    if y[i] not in res1:
        res1+=y[i]
res2=''
for i in res:
    if i in res1:
        res2+=i

print(res)
print(res1)
print(res2)

o1=set(x)
o2=set(y)
print(o1)
print(o2)
out=o1&o2
print(out)


