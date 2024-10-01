x="Sheena loves eating apple and mango. Her sister also loves eating apple and mango"
y=[]
x_clean=x.replace('.','')
y.extend(x_clean.split(' '))

duplicates= [i for i in y if y.count(i) > 1] 
duplicates_clean=set(duplicates)
print(duplicates_clean)
print(y)


